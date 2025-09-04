const form = document.getElementById("survey-form");
const resultDiv = document.getElementById("result");
const output = document.getElementById("output");

// 결과표시함수
function displayResult(data) {
  output.innerHTML = `
    <strong>이름:</strong> ${data.name}<br>
    <strong>이메일:</strong> ${data.email}<br>
    <strong>나이:</strong> ${data.age}<br>
    <strong>만족도:</strong> ${data.satisfaction}<br>
    <strong>관심분야:</strong> ${data.interests.join(", ") || "선택 없음"}<br>
    <strong>추가의견:</strong> ${data.feedback || "없음"}<br>
    `;
  resultDiv.style.display = "block";
}

// localstorage에서 불러오기
window.addEventListener('load', ()=> {
  const saveData = localStorage.getItem('surveyData');
  if(saveData) {
    const data = JSON.parse(saveData);
    displayResult(data);
  }
});

// 제출 이벤트 처리
form.addEventListener('submit', event => {
  event.preventDefault(); // 새로고침 방지

// 입력값 수집
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const age = document.getElementById('age').value;
  const satisfaction = document.querySelector("input[name='satisfaction']:checked").value;
  const interests = Array.from(document.querySelectorAll("input[type='checkbox']:checked")).map(cb => cb.value);
  const feedback = document.getElementById('feedback').value;

  const surveyData = {name, email, age, satisfaction, interests, feedback};
// localStorage 저장
  localStorage.setItem('surveyData', JSON.stringify(surveyData));
// 결과 표시
  displayResult(surveyData);
});
  

