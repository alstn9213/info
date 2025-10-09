# @Service
- @Service 애너테이션이 사용된 모든 클래스를 객체로 만들어 스프링 컨테이너에 두고 관리한다. 그리고 컨트롤러 대신 서비스 객체가 직접 리포지터리를 사용할 것이므로 회원 리포지터리 객체를 전달받는다. 만약 DTO 계층을 만들어 사용할 경우, 서비스 클래스에는 엔티티 객체를 DTO 객체로 변환하기 위한 메서드를 따로 정의해야하지만 
```java
@Service
@RequiredArgsConstructor
public class ArticleService {
    private final MemberRepository memberRepository;
    private final ArticleRepository articleRepository;
//  엔티티 객체를 DTO 객체로 변환하기 위한 메서드
    private ArticleResponse mapToArticleResponse(Article article) {
        return ArticleResponse.builder()
                .id(article.getId())
                .title(article.getTitle())
                .description(article.getDescription())
                .created(article.getCreated())
                .updated(article.getUpdated())
                .memberId(article.getMember().getId())
                .name(article.getMember().getName())
                .email(article.getMember().getEmail()).build();
    }
}
```
Record를 사용할 경우 그럴 필요가 없다. 여기서 “별도의 변환 메서드”가 필요 없어 보이는 이유는,
레코드가 이미 자동으로 생성자, getter, equals, hashCode, toString 등을 만들어주기 때문이다. 즉, DTO 변환이 사실상 한 줄짜리 “생성자 호출”로 끝나는 것이다.

- “자동 변환”처럼 보이지만 사실은 우리가 직접 호출하고 있다.
```java
public final class MemberDto {
    private final Long id;
    private final String name;

    public MemberDto(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    public Long id() { return id; }
    public String name() { return name; }
}

```
레코드는 단지 이런 코드를 자동으로 만들어줄 뿐이다. 즉, 우리가 new MemberDto(member.getId(), member.getName())라고 부르는 순간 그건 “직접 변환”이지, 자동 변환이 일어나는 건 아니다.