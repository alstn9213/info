// DOM 요소 가져오기위한 변수 선언 및 초기화
const todoInput = document.getElementById('todo-input'); 
const addBtn = document.getElementById('add-btn');
const todoList = document.getElementById('todo-list');

//  처음 페이지에 들어갔을 때 localStorage를 참조해서 기존 todo데이터가 있다면 가지고 와야한다.
// 값이 있으면 true 없으면 false
let todos = JSON.parse(localStorage.getItem('todos')) || [];
// localStorage.getItem('todos')에 데이터가 있으면 true이기때문에 JSON으로 바꿔주고
// 아무런 데이터가 없으면 빈배열을 저장
// console.log(todos); // 결과값 배열 -> 맨처음에 localStorage를 뒤지면 빈 배열이 저장된다. 이후에 배열 내부의 element들에 객체를 추가했다.
// localstorage에 저장되는 것은 Js객체가 아니라 배열이라는 점에 주목하자.


// Todo 리스트를 불러오는 과정이 필요하다.
// 페이지에 처음 들어갔을 때의 로직
function renderTodos(){
  // 기존 todo list를 초기화 -> 추가했을 때 누적 안되게
  // todoList =/= todos
  todoList.innerHTML = '';

  // todos 배열을 반복문으로 목록을 생성
  todos.forEach((todo, index) => {
    // todos의 반복을 돌면 내부 element가 있을 텐데 
    // 그때마다 li 태그를 생성한다는 의미
    // 웬만하면 forEach() / map() 메서드에는 두개 이상의 인수가 요구된다고 생각하자
    // 보통은 첫번째가 반복문 돌때의 element이름
    //  두번째가 index

    // 각 todo는 JS객체에 해당하는 거고 이걸 페이지 상에서 보여주기 위해서는 ul태그의 자식인 li태그가 필요하다.

    // 그럼 li는 지역변수다.
    const li = document.createElement('li');
    // li 태그만 만들었지 클래스 이름 안정했으니까
    li.className = 'todo-item';
    if(todo.completed) { // localStorage의 'todos' key 내부를 확인했을 때 배열로 저장돼있고, 거기 내부에 JS객체가 있는데, 그 객체가 현재 todos라고 이름 붙여져 있다. 그 todos들은 text라는 key, completed라는 key를 가지고 있다.
      //  그 completed는 자료형이 boolean이었고, true / false인지에 따라서 조건문의 실행여부가 결정된다.
      // .css 파일에서 completed 속성 부분을 적용해주기위해 쓴 코드라인이다.
      // completed가 true라면 할일이 완료되었음을 표시하기 위해서 css상 차이를 만들었는데, 그걸 적용하기 위함이다.
      li.classList.add('completed');
    }
    //  js 객체상의 key가 completed인 애의 value가 true라면 li 태그에 completed라는 속성을 추가해주는데, 이게 추가되면 .css에서 정의된 추가 스타일을 적용하기 위한 것이다.(취소선, 배경색 등).

    // li 태그의 자식 요소로 input checkbox / span / button으로 이루어져 있기때문에 각각을 또 요소로 만들 필요가 있다.

    // 체크박스 - input 태그니까
    const checkbox = document.createElement('input');
    // 근데 type이 text가 아니라 checkbox니까
    checkbox.type = 'checkbox';
    checkbox.checked = todo.completed;
    // todo.completed는 boolean 자료형이다. 
    // checked 자체는 true false와 상관없이 계속 유지된다.
    // input의 type이 checkbox라면 checked하고 =""가 없는 애가 있었다. <input type="checknox" checked> 형태였다.

    // 텍스트 내용 생성 - span태그
    // div가 아니라 span인 이유자체도 생각할 필요가 있다.
    // div - 컨테츠가 있는 가로줄 전체가 영역
    // span - 컨텐츠가 있는 길이만큼만 영역
    const span = document.createElement('span');
    span.className = 'todo-text';  // 마찬가지로 CSS적용을 위해서
    span.textContent = todo.text; // 내용이 있는거니까 배열내의 element인 JS객체의 text라는 키의 value를 span태그의 내부에 집어 넣어서 페이지상에 출력

    // 삭제 버튼 - button
    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-btn';
    deleteBtn.innerHTML = '&times'; // x기호

    // 요소들을 li 변수에 추가해야한다. li내부에 체크박스/span/button 이 있으니까.
    li.append(checkbox);
    li.append(span);
    li.append(deleteBtn);

    // 그리고 이 li를 <ul> 태그에 추가해야 한다.
      todoList.appendChild(li);

    // 이벤트리스너 추가
    //  체크박스 변경 이벤트
    checkbox.addEventListener('change', () => {
      todos[index].completed = checkbox.checked; // checkbox가 type이고, checked는 속성에 해당했다.
      // 완료 상태에 따라 CSS 클래스를 토글
      li.classList.toggle('completed', checkbox.checked);
      saveTodos();
    });

    // 삭제 버튼 클릭 이벤트
    deleteBtn.addEventListener('click', () => {
      // 삭제할 항목의 텍스트를 이용해서 배열내에서 정확한 인덱스를 찾아낼 것이다.
      // 보통은 index로 내용을 확인하지만 계속 삭제를 하면 index넘버가 바뀐다.
      // 그래서 input에 입력했던 내용을 근거로 index를 역을 찾아낼 예정이다.
      const itemText = span.textContent; // 얘를 쓰는 이유는 .trim()을 쓰는 바람에 공백을 날렸기 때문이다.

      // 배열 내에서의 내용과 span태그의 내에서의 내용은 같은 index를 뽑아내서 itemIndex변수에 저장
      const itemIndex = todos.findIndex(item => item.text === itemText);

      if(itemIndex !== -1) { // 일치하는 인덱스가 없으면 -1이다.
        todos.splice(itemIndex, 1); // itemIndex에 해당하는 거 element 하나를 삭제
        li.remove();
        saveTodos();
      }
    });
  });
}

  function saveTodos() {
    // localStorage에 저장한다는 의미였으니까
    localStorage.setItem('todos', JSON.stringify(todos));
    // 1번 매개변수 - key
    // 2번 매개변수 - 그 키에 들어가는 value
    localStorage.setItem('temp', '안녕'); // 오해할까봐 추가한 코드. 여기는 value가 string이다. 
  }

  function addTodo() {
    const todoText = todoInput.value.trim(); // trim() 공백제거 메서드
    if(todoText === '') {
      alert('내용을 입력하세요');
      return; // 메서드를 종료시키겠다는 의미. 이 아래의 코드들은 실행이 되지않는다.
    } 

    // input 창에 내용이 있다면 내용이 들어갈 JS객체 선언
    const newTodo = {
      text: todoText,
      completed: false, // 초기생성시에 무조건 false로 고정
    };

    // todos에 새로운 todo를 추가
    todos.push(newTodo);

    // 추가한 이후에 input 태그 내의 내용을 비우는 역할
    todoInput.value = '';

    // 주의 : splice() =/= slice()
    renderTodos(); // 추가버튼 누르고 나서 다시 (갱신된) 리스트 가지고 와야하니까 renderTodos() 함수호출
    saveTodos(); // 그리고 localStorage에도 저장해줘야하니까 saveTodos()함수 호출

    // 그러면 어차피 renderTodos() 할때 saveTodos()가 필수인것같은데 함께 묶어서 쓰면되지않나하는 의문이 들 수 있다.
    // 메서드 하나당 기능 하나라고 생각해야한다.
  }

  //  '추가' 버튼 클릭 이벤트
  addBtn.addEventListener('click', addTodo); // button 태그의 onclick속성이다. -> 두 번째 인자로 addTodo함수를 넣었는데 addTodo()가 아니라는 점에도 주목하자

  // 엔터 키 입력 이벤트
  todoInput.addEventListener('keydown', (event) => {
    if(event.key === 'Enter') {
      addTodo(); // input태그에 Enter키 입력을 감지하면 addTodo(); 함수를 호출할 것.
    }
  });

  // 새로고침했을 때 renderTodos()가 호출되어야함.
  window.onload = renderTodos();