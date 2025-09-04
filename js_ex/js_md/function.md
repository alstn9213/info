# for문 안의 즉시실행함수

즉시 실행 함수(IIFE, Immediately Invoked Function Expression)는 정의하자마자 실행되는 함수이다.
```js
(function () {
  console.log("실행됨!");
})();

```
이 코드는 한 번만 실행된다.

그런데 이걸 for문 안에 넣으면, for 반복 횟수만큼 매번 새로운 함수가 정의되고 즉시 실행된다.

```js

for (let i = 0; i < 3; i++) {
  (function () {
    console.log("실행됨!", i);
  })();
}

```

IIFE 자체는 "작성될 때 바로 실행되는 성질"을 가진 거고, for 안에서 계속 작성하면 반복마다 매번 실행된다.
즉, for문 안에서 IIFE를 쓰면, 반복할 때마다 "새로운 함수 객체"가 만들어지고 실행된다.