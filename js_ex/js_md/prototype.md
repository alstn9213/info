# 프로토타입

## 프로토타입의 생성시점
객체는 리터럴 표기법 또는 생성자 함수에 의해 생성되므로 결국 모든 객체는 생성자 함수와 연결 돼 있다. 프로토타입은 생성자 함수가 생성되는 시점에 더불어 생성된다. 

생성자 함수로서 호출할 수 있는 함수는 함수 정의가 평가되어 함수 객체를 생성하는 시점에 프로토타입도 더불어 생성된다.

```js
// 함수 객체를 생성하는 시점에 프로토타입도 더불어 생성된다.
console.log(Person.prototype); // {constructor: f}

// 함수 정의가 console.log()보다 먼저 평가된다. 
// Person 생성자 함수가 평가되고 함수 객체가 된다. 
// 이때 프로토타입도 더불어 생성된다.
// 생성된 Person프로토타입은 Person생성자 함수의 prototype프로퍼티에 바인딩된다.
function Person(name) {
  this.name = name;
};
```

## 빌트인 생성자 함수와 프로토타입 생성 시점
모든 빌트인 생성자 함수는 전역객체가 생성되는 시점에 생성된다. 생성된 프로토타입은 빌트인 생성자 함수의 prototype 프로퍼티에 바인딩된다. 이처럼 객체가 생성되기 이전에 생성자 함수와 프로토타입은 이미 객체화 되어 존재한다. 이후 객체를 생성하면 프로토타입은 생성된 객체의 `[[Prototype]]` 내부 슬롯에 할당된다.

## 객체 생성 방식과 프로토타입의 결정
모든 객체는 어떤 방식으로 생성되든 추상연산 OrdinaryObjectCreate에 의해 생성된다. 추상 연산 OrdinaryObjectCreate는 필수적으로 자신 생성할 객체의 프로토타입을 인수로 전달받는다. 인수로 전달받은 프로토타입을 자신이 생성한 객체의 `[[Prototype]]` 내부 슬롯에 할당한 다음, 생성한 객체를 반환한다. 즉, 프로토타입은 추상연산 OrdinaryObjectCreate에 전달되는 인수에 의해 결정된다.

```js

const obj = {x:1};
// 객체리터럴에 의해 생성된 obj객체는 Object.prototype을 상속받는다.
console.log(obj.constructor === Object);
console.log(obj.hasOwnProperty('x'));
```

## 객체리터럴과 Object 생성자함수에 의한 객체 생성방식의 차이
둘의 차이는 프로퍼티를 추가하는 방식에 있다. 객체리터럴 방식은 객체 리터럴 내부에 프로퍼티를 추가하지만 Object 생성자 함수 방식은 일단 빈 객체를 생성한 이후 프로퍼티를 추가해야한다.

## 생성자 함수에 의해 생성된 객체의 프로토타입
new 연산자와 함께 생성자함수를 호출하여 인스턴스를 생성하면 다른 객체생성방식과 마찬가지로 추상 연산 OrdinaryObjectCreate가 호출된다. 이때 추상 연산 OrdinaryObjectCreate에 전달되는 프로토타입은 생성자 함수의 prototype 프로퍼티에 바인딩되어 있는 객체다.

## 프로토타입 체인
```js

function Person(name) {
  this.name = name;
}
Person.prototype.sayHello = function() {
  console.log(`Hi! My name is ${this.name}`);
};

const me = new Person('Lee');
console.log(me.hasOwnProperty('name')); // true

console.log(me.sayHello()); // 자바스크립트는 함수안에 return값을 입력하지않으면 undefined를 할당한다. 그래서 결과값이 
// Hi! My name is Lee
//  undefined 
```

프로토타입 체인의 최상위에 위치하는 객체는 언제나 Object.prototype이다. 따라서 모든 객체는 Object.prototype을 상속받는다. Object.prototype의 프로토타입, 즉 `[[Prototype]]` 내부 슬롯의 값은 null이다. 이처럼 자바스크립트 엔진은 프로토타입 체인을 따라 프로퍼티/메서드를 검색한다. 프로토타입 체인은 상속과 프로퍼티 검색을 위한 메커니즘이다. 이에 반해, 프로퍼티가 아닌 식별자는 스코프체인에서 검색한다. 즉, 스코프 체인은 식별자 검색을 위한 메커니즘이다.
```js
me.hasOwnProperty('name');
```
위 예제에서 먼저 스코프체인에서 me 식별자를 검색한다. me 식별자를 찾으면 me 객체의 프로토타입 체인에서 hasOwnProperty 메서드를 검색한다.
이처럼 스코프 체인과 프로토타입 체인은 서로 연관없이 별도로 동작하는 것이 아니라 서로 협력하여 식별지와 프로퍼티를 검색하는데 사용된다.

