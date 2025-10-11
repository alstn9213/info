# Stream
- 각 컬렉션 클래스에는 같은 기능의 메서드들이 중복해서 정의 돼 있다. 예를 들어 List를 정렬할 때는 Collection.sort()를 사용해야하고, 배열을 정렬할 때는 Arrays.sort()를 사용해야한다. 이러한 문제점들을 해결하기위해 만든것이 `스트림(Stream)` 이다. 스트림은 데이터 소스를 추상화하고, 데이터를 다루는데 자주 사용되는 메서드들을 정의해 놓았다. 데이터 소스를 추상화하였다는 것은, 데이터 소스가 무엇이던 간에 같은 방식으로 다룰수 있게 되었다는 것과 코드의 재사용성이 높아진다는 것을 의미한다.

예를 들어 문자열 배열과 같은 내용의 문자열을 저장하는 List가 있을 때,
```java
String[] strArr = {"aaa", "ddd", "ccc"};
List<String> strList = Arrays.asList(strArr);
```
이 두 데이터 소스를 기반으로 하는 스트림은 다음과 같이 생성한다.
```java
Stream<String> strStream1 = strList.stream();
Stream<String> strStream2 = Arrays.stream(strArr);
```

## Stream의 특징
1. 스트림은 데이터 소스를 변경하지않는다.
    - 스트림은 데이터 소스로부터 데이터를 읽기만할 뿐, 데이터소스를 변경하지않는다.
2. 스트림은 일회용이다.
3. 스트림은 작업을 내부 반복으로 처리한다.
    - 내부 반복이라는 것은 반복문을 메서드의 내부에 숨길 수 있다는 것을 의미한다. forEach()는 스트릠에 정의된 메서드 중에 하나로 매개변수에 대입된 람다식을 데이터 소스의 모든 요소에 적용한다.
    다음 둘은 같다.
  `for(String str : strList) System.out.println(str);`
  `stream.forEach(System.out::println);`
  즉 forEach()는 for문을 메서드 안으로 넣은 것이다. 반복할 작업은 매개변수로 받는다.

