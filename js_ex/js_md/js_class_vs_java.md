# 자바의 클래스 vs. 자바스크립트의 클래스

자바스크립트는 클래스 기반 언어가 아니지만 자바같은 클래스 기반의 언어 사용자가 자바스크립트에 빠르게 익숙해 질 수 있도록 클래스 기능 또한 제공한다.
다만 자바와 자바스크립트가 제공하는 클래스의 내부 동작 방식은 서로 다르다.

## 자바스크립트의 클래스

자바스크립트에서 class 문법은 사실 **문법적 설탕(syntactic sugar)** 이다. 겉으로는 자바의 클래스처럼 보이지만 내부적으로는 여전히 **생성자 함수(constructor function)**와 프로토타입 기반 객체 지향을 사용한다.

```js
class Person {
  constructor(name) {
    this.name = name;
  }

  sayHello() {
    console.log(`Hello, I am ${this.name}`);
  }
}

const p1 = new Person("홍길동");
p1.sayHello(); // Hello, I'm 홍길동

```

위 코드는 사실 아래와 같은 생성자 함수 + prototype 방식과 동일하다.

```js
const p1 = new Person("홍길동");
p1.sayHello(); // Hello, I'm 홍길동
function Person(name) {
  this.name = name;
}
Person.prototype.sayHello = function() {
  console.log(`Hello, I'm ${this.name}`);
};
```

즉, **자바스크립트 클래스는 특별한 문법일 뿐, 본질은 함수(Function)**

## 자바의 클래스

반대로 **자바(Java)**에서는 클래스가 언어의 핵심 단위이고, 함수가 아니다.
자바의 클래스는 객체의 설계도(blueprint) 역할을 하며, 필드(속성)와 메서드(동작)를 정의한다.

```java
public class Person {
    String name;

    // 생성자(Constructor)
    public Person(String name) {
        this.name = name;
    }

    public void sayHello() {
        System.out.println("Hello, I'm " + name);
    }
}

public class Main {
    public static void main(String[] args) {
        Person p1 = new Person("홍길동");
        p1.sayHello(); // Hello, I'm 홍길동
    }
}
```

Person은 함수가 아니다. 자바에서 **클래스는 타입(type)** 이다.
클래스 자체는 실행 가능한 함수가 아니라 객체를 찍어내는 틀이다.