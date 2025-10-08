# @Builder

```java
@Entity
@NoArgsConstructor
@Builder
public class Member {
    private String name;
    private int age;
}

```
이 경우 @Builder 에 오류가 난다.
```java
@Entity
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Member {
    private String name;
    private int age;
}

```
그래서 @AllArgsConstructor를 추가해야하는데, 그 이유는 @Builder가 내부적으로 생성자를 필요로 하기 때문이다. 즉, @Builder는 **클래스 내부에 있는 “모든 필드를 매개변수로 받는 생성자”**를 기반으로 동작한다. 그런데 @NoArgsConstructor만 있으면 @NoArgsConstructor는 “매개변수가 없는 기본 생성자”만 생성한다. 그래서 @AllArgsConstructor가 모든 필드를 매개변수로 받는 생성자를 만들어 주면 Builder가 정상작동한다. 그런데

```java
@Data
@Builder
public class ArticleRequest {
    private String title;
    private String description;
}

```
이 경우엔 생성자 관련 애너테이션이 없음에도 빌더가 작동한다. 왜냐하면 Lombok의 @Builder는, 생성자가 명시되어 있지 않으면 클래스의 모든 필드를 인자로 받는 "가상의 생성자"를 만들어 사용하기 때문이다. 그럼 왜 아까는 그런 기능이 발동하지 않았을까? 
```java
@Entity
@NoArgsConstructor
@Builder
public class Member {
    private String name;
    private int age;
}

```
이 경우는 JPA가 기본 생성자를 반드시 필요로 하기 때문에, Lombok이 “빌더용 private 생성자”를 만들면 그게 JPA가 사용하는 생성자 규칙(public 혹은 protected 무인자 생성자`)과 충돌할 수 있다. 또한, 엔티티 클래스에 final 필드나 @Id 같은 제약이 있으면 Lombok이 자동 생성자 주입을 제한하기 때문에, @AllArgsConstructor를 명시적으로 붙여줘야 @Builder가 정확히 어떤 생성자를 써야 하는지 알게 된다.