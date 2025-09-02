# 값의 전달

JS에서 원시값은 복사에 의한 전달, 객체는 참조에 의한 전달이다. 그래서 객체와 변수의 값을 바꾸는 함수를 만들었을 때, 결과는 다음과 같다.
```js
function changeVal(primitive, obj) {
  primitive += 100;
  obj.name = 'Kim';
}

var num = 100;
var person = {name: 'Lee'};
console.log(num);
console.log(person);
changeVal(num, person);
// 원시값은 원본이 훼손되지않는다.
console.log(num);
// 객체는 원본이 훼손된다.
console.log(person);
```

- 참고
`const person = {name:'Lee'};` 같은 식으로 객체를 const 변수에 할당하더라도 `person.name='Kim';` 으로 객체의 프로퍼티 값을 바꿀 수 있다. 이는 const의 기능이 어디까지나 변수의 재할당을 금지하는 것이지 객체의 프로퍼티의 변경을 제한하는 것이 아니기때문이다. 
