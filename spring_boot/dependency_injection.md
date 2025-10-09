# 의존성 주입
- MemberService가 Bean으로 등록될 때, 스프링은 “생성자에 MemberRepository가 필요하다보고, 컨테이너 안에 등록된 MemberRepository 빈을 찾아 자동으로 주입(Injection) 해준다. 그래서 우리는 new MemberRepositoryImpl() 같은 걸 직접 만들 필요가 없다.
- 서비스 계층에서 리포지토리 인터페이스 객체를 “new”로 만들지 않아도 자동으로 주입되는 이유는 바로 Spring의 의존성 주입(Dependency Injection, DI) 덕분이다.
  이 기능이 동작하게 만드는 핵심 애너테이션은 @Repository , @Service, @Autowired 세 가지 중 일부 조합이다.

  1. @Repository
     - @Repository가 붙은 인터페이스는 Spring이 데이터 접근 계층이라고 인식함. 그리고 Spring Data JPA가 실행 시점에 **이 인터페이스의 프록시 구현체(가짜 객체)**를 자동 생성해서 Spring 컨테이너에 Bean으로 등록해둔다.
  
  2. @Service
     - 이 애너테이션이 붙은 클래스도 Bean으로 등록됨.

  3. @Autowired
     - 이 애너테이션이 붙으면 스프링 컨테이너가 자동으로 의존 객체를 주입
     
## @Autowired의 생략
  - **@RequiredArgsConstructor**를 쓰면 final 필드를 매개변수로 받는 생성자를 자동으로 만들어주고, Spring이 그 생성자를 통해 주입하기 때문에 @Autowired를 생략해도 된다. 즉, @Autowired 없이도 DI가 되는 이유는 Spring이 **“생성자가 하나뿐인 클래스는 그 생성자에 자동 주입한다”** 라는 규칙을 따르기 때문이다.
```java
@RequiredArgsConstructor
@Service
public class MemberService {
    private final MemberRepository memberRepository;
}

```
- Spring은 @Service를 보고 이 클래스를 Bean으로 등록하려고 함. 즉, “MemberService를 관리해야겠다”고 판단함. 그리고 등록하려는 클래스의 생성자를 검사한다.
이때 생성자가 단 하나뿐이라면 이 생성자를 써서 객체를 만든다. 그 다음 생성자의 매개변수 타입(MemberRepository)을 확인함. 만약 스프링 컨테이너에 같은 타입(MemberRepository)의 Bean이 등록되어 있으면
그 Bean을 찾아서 자동으로 넣어줌 (Dependency Injection).
```java
@Service
public class MemberService {

    private final MemberRepository memberRepository;

    // 생성자가 하나뿐임
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }
}


```

- 만약 생성자가 여러 개라면 Spring이 “어떤 생성자를 써야 할지” 모르니까

```java
@Service
public class MemberService {

    private final MemberRepository memberRepository;
    private final EmailService emailService;

    @Autowired
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
        this.emailService = null;
    }

    public MemberService(MemberRepository memberRepository, EmailService emailService) {
        this.memberRepository = memberRepository;
        this.emailService = emailService;
    }
}

```
스프링이 어느 생성자로 주입해야할지 알려주기위해 @Autowired로 지정해야 함.