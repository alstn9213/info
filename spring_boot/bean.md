# @Bean
- 메서드에 @Bean을 붙이면 스프링이 이 메서드의 반환값을 스프링 컨테이너(Bean Factory)에 등록한다.

- 스프링에서는 클래스 전체를 Bean으로 등록할 수도 있고, 메서드의 반환값을 Bean으로 등록할 수도 있다. 다음은 “애플리케이션이 실행되자마자 자동으로 실행되는 코드 블록” 이다. 즉, 테스트용 데이터를 자동으로 넣기 위한 초기화 코드다. 
```java
@Bean
CommandLineRunner runner(UserRepository userRepository,
                         TodoRepository todoRepository,
                         PasswordEncoder passwordEncoder) {
    return args -> {
        User user = new User("user", passwordEncoder.encode("user"), "USER");
        userRepository.save(user);
        todoRepository.save(new Todo(user,"스프링부트 프로젝트 만들기"));
        todoRepository.save(new Todo(user,"리액트 연동하기"));
    };
}

```
CommandLineRunner는 스프링 부트가 애플리케이션을 모두 초기화한 뒤 자동으로 실행하는 인터페이스이다.

- 이 코드는 PasswordEncoder 타입의 스프링 Bean 객체를 등록하는 것이다. 이제 스프링이 BCryptPasswordEncoder 객체를 자동 주입(@Autowired)할 수 있다.
```java
@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
}
```
