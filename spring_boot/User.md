# User
- User 클래스는 스프링 시큐리티의 구현체이다. 즉, User 클래스는 `UserDetails 인터페이스의 “구현체(implementation)”`이다.
- UserDetails는 인터페이스이다. 인터페이스라서 생성자나 빌더를 가질 수 없다. 즉, UserDetails.builder()같은건 불가능하다.
```java
public interface UserDetails extends Serializable {
    Collection<? extends GrantedAuthority> getAuthorities();
    String getPassword();
    String getUsername();
    boolean isAccountNonExpired();
    boolean isAccountNonLocked();
    boolean isCredentialsNonExpired();
    boolean isEnabled();
}
```
그래서 UserDetails 객체를 만들때 우리가 흔히 쓰는 건 User 클래스의 빌더이다.
```java
import org.springframework.security.core.userdetails.User;
// UserDetails는 인테페이스이기 때문에 객체로 만들 수 없다. 아래의 예시는 User를 사용해 객체를 만든 것이고 UserDetails는 타입을 선언한 것이다.
        UserDetails user = User.builder()
    .username("test")
    .password("1234")
    .roles("USER")
    .build();

```
여기서 .builder()가 가능한 이유는 User 클래스(스프링 시큐리티가 제공하는 구현체)가 내부적으로 @Builder가 적용된 정적 내부 클래스(Builder)를 제공하기 때문이다.

```java
public class User implements UserDetails {
    private String username;
    private String password;
    private Set<GrantedAuthority> authorities;

    // 빌더 클래스 내부에 정의되어 있음
    public static UserBuilder builder() {
        return new UserBuilder();
    }

    public static class UserBuilder {
        private String username;
        private String password;
        private List<GrantedAuthority> authorities = new ArrayList<>();

        public UserBuilder username(String username) { ... }
        public UserBuilder password(String password) { ... }
        public UserBuilder roles(String... roles) { ... }
        public UserDetails build() { ... }
    }
}

```
즉, 이건 롬복의 @Builder가 아니라 스프링 시큐리티 개발자들이 직접 작성한 빌더 패턴 클래스이다.(직접 UserBuilder를 구현해둔 형태.)

