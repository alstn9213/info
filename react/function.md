# React의 함수들
1. useState()
- 매개변수로 받은 값을 상태값에 전달하고, 상태값과 상태변경함수를 반환한다.

```jsx
// useState는 사실
const [count1, setCount] = useState(0); 
// 아래처럼 동작한다.
const stateArray = useState(0);
const count1 = stateArray[0];     // 현재 상태값 (state)
const setCount1 = stateArray[1];  // 상태를 바꾸는 함수 (state updater function)
```

즉, useState()는 배열 [state, setState]를 반환한다.
0번 인덱스의 state는 현재 상태 값 (count1)을 1번 인덱스의 setState는 상태를 변경하라고 React에게 "요청"하는 함수 (setCount1)이다.
이때, setCount1은 `React 내부(라이브러리 코드)`에서 만들어진 함수이다.
React는 컴포넌트가 useState()를 호출할 때마다, 내부적으로 특정 위치(“state slot”)에 상태를 저장하고, 그 상태를 변경할 수 있는 함수를 만들어서 두 번째 값으로 반환한다.
즉, setCount1은 React가 useState를 실행할 때 `직접 만들어서 돌려주는 함수` 이다.