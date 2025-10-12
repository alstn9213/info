# UserDetailsService
- 사용자가 로그인화면에서 입력한 이름과 패스워드를 애플리케이션 설정파일에서 정의한 이름과 패스워드를 사용해 비교하는 것이 아니라, 
  1. 입력된 사용자 이름에 해당하는 사용자 정보를 찾아 패스워드가 무엇인지
  2. 해당 계정이 사용 가능한지
  3. 패스워드의 유효기간이 지나 변경이 필요한지 
등의 상세한 사용자 정보(UserDetails)를 조회하기 위한 객체가 필요하다. 이를 위해 스프링 시큐리티는 `UserDetailsService`인터페이스를 정의하고있으며, 이 인터페이스를 구현하는 스프링 빈 객체를 생성해 등록하면 된다.
```java
public interface UserDetailsService {
    UserDetails loadUserByUsername(String username) throws UsernameNotFoundException;
}
```

`UserDetails loadUserByUsername(String username);`메서드는 로그인 화면에서 입력한 사용자 이름을 전달받아 이에 해당하는 사용자의 정보를 조회하고, 이를 사용해 UserDetails 객체를 만들어 반환하도록 구현하면 된다.

## PasswordEncoder
- 스프링 시큐리티에서 사용자 패스워드는 보안에 매우 민감한 정보이므로 그대로 노출되면 안된다. 따라서 반드시 단방향 인코딩을 하는데, 이를 위해 스프링 시큐리티는 `PasswordEncoder` 라는 인터페이스를 제공한다. 패스워드 단방향 인코딩을 위한 여러가지 알고리즘이 있는데, 스프링 시큐리티가 제공하는 패스워드 인코더인 `BCryptPasswordEncoder` 를 사용하는 것도 한 방법이다.

### BCryptPasswordEncoder
- BCryptPasswordEncoder는 기본적으로 PasswordEncoder 인터페이스를 구현하므로, 다음과 같이 스프링 빈 객체로 만들어 등록하고 UserDetails 객체를 생성할 때 BCrypt 방식으로 인코딩된 패스워드를 사용하면 된다.

```java
@Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
```
스프링 시큐리티는 스프링 컨테이너에 PasswordEncoder 인터페이스를 구현한 스프링 빈 객체가 있을 경우, 사용자가 입력한 패스워드와 UserDetailsService를 통해 전달된 UserDetails의 암호화된 패스워드를 직접 비교하지 않고 PasswordEncoder의 matches()메서드를 통해 비교한다.

## 커스텀 사용자 인증 서비스 
- 별도의 회원 관리를 위한 테이블을 만든 다음, 이를 사용하도록 UserDetailsService를 직접 작성하거나 애플리케이션에서 관리하는 회원 정보를 사용하도록 UserDetails 객체를 확장할 수 있다.

