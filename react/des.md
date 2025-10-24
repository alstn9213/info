# 객체 구조분해


```js
// userObj에서 name과 age를, 그리고 clickHandler를 바로 꺼내 쓰겠다!
function User({userObj: {name, age}, clickHandler}) {
  return (
    <>
      <p>name: {name}</p> {/* props.userObj.name 대신 name 바로 사용 */}
      <p>age: {age}</p>   {/* props.userObj.age 대신 age 바로 사용 */}
      <button onClick={clickHandler}>클릭</button>
    </>
  );
}
```
- 이 코드는 props라는 객체를 통째로 받는 대신, props 객체를 받자마자 "분해"해서 그 안에 있는 userObj의 name, age와 clickHandler를 바로 변수로 꺼내 쓰겠다는 뜻이다.
`{userObj: {name, age}, clickHandler}` 이 부분이 바로 구조 분해 할당이다.
sd