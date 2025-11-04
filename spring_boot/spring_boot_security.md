# security

## AccessKeyFilter

- RESTful API는 URL만 알면 누구나 API를 호출해 회원정보를 생성하거나 특정한 회원이 작성한 게시글을 조회할 수 있다. 이를 막기위해 클라이언트에 대한 허가 절차가 필요하다. 스프링부트에서 제공하는 필터 기능을 사용하면 HTTP 헤더에 포함된 엑세스 키를 컨트롤러 앞단에서 검증할 수 있다. 즉, 엑세스 키를 검증하는 필터를 작성해 컨트롤러 앞 단에 배치함으로써 정상적인 엑세스키가 포함된 API 호출에 대해서만 컨트롤러에게 전달하고, 엑세스 키가 헤더에 포함되어 있지 않거나 엑세스키가 정상이 아닌 경우, 필터에서 바로 클라이언트로 401 Unauthorized 오류를 반환하도록 구현하면 된다.

- 웹 필터는 일반적으로 `OncePerRequestFilter` 를 상속받아 작성하는데, 이 경우 한번의 요청에 대해 한번만 필터를 거치도록한다. 실제 필터를 구현하기 위해 Filter 인터페이스를 구현하는 대신 OncePerRequestFilter를 상속받았으므로, 필터는 doFilter()대신 doFilterInternal()을 오버라이드해 작성한다.

```java
package com.example.demo2.filter;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebFilter;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.http.HttpStatus;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;

@WebFilter(urlPatterns = "/api/*")
public class AccessKeyFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        String authorization = request.getHeader("Authorization");
        if(authorization != null && authorization.startsWith("Bearer")) {
            String token = authorization.replace("Bearer", "").trim();
            if("hanbit-access-key".equals(token)) {
                filterChain.doFilter(request, response);
                return;
            }
        }
        response.setStatus(HttpStatus.UNAUTHORIZED.value());
    }
}
```

전달된 HttpServletRequest 파라미터에서 Authorization 헤더를 구한 후 Bearer를 제거한 엑세스 키가 'hanbit-access-key' 인지 검증한 다음, 정상적인 경우 다음 단계로 진행하고 아니면 인증 오류 401 Unauthorized를 반환한다.
이때 `request.getHeader("Authorization");`의 헤더는 HTTP 요청(Request)의 헤더(Header) 중에서 "Authorization" 이라는 이름을 가진 헤더 값을 가져오는 것이다.

```pgsql
GET /api/users HTTP/1.1
Host: localhost:8080
Authorization: Bearer hanbit-access-key
Content-Type: application/json
```

즉, 클라이언트(브라우저나 앱)가 서버에 보낼 때 함께 전송한 HTTP 요청 헤더의 일부이다.
여기서는 "Authorization" 이라는 이름을 가진 `Authorization: Bearer hanbit-access-key`를 의미한다.
서버(스프링 부트)는 이 요청을 받으면 HttpServletRequest 객체로 파싱해서 필터나 컨트롤러에서 다루게 되고,
그때 request.getHeader("Authorization") 을 호출하면 "Bearer hanbit-access-key" 라는 문자열을 돌려준다.

- Bearer

  - HTTP 인증 헤더의 표준 형식에 따르면 Authorization 헤더의 형식은 `Authorization: <인증 방식> <인증 자격>`으로 되어있다. 형식을 정해뒀으니 따라야한다.
  - `Bearer`는 “이 토큰이 어떤 방식으로 인증되는지”를 명시하는 표준 키워드이다. Bearer는 영어로 “소지자”, “가지고 있는 사람”이라는 뜻이다. 즉, `“이 토큰을 가진 사람은 인증된 사용자로 간주한다”`는 의미이다.
    Authorization: Bearer 'token'에서 "이 요청을 보낸 사람은 'token' 을 가지고 있으므로, 그 토큰이 유효하다면 접근을 허락해달라"라는 뜻이다.

## AuthenticationFilter
- AuthenticationFilter는 요청 객체(HttpServletRequest)에서 username과 password를 추출해서 토큰을 생성한다.

```java
package com.project.team.Security;

import com.project.team.Service.UserDetailsServiceImpl;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
@Component
public class AuthenticationFilter extends OncePerRequestFilter {

    private final JwtService jwtService;
    private final UserDetailsServiceImpl userDetailsService;

    public AuthenticationFilter(JwtService jwtService, UserDetailsServiceImpl userDetailsService) {
        this.jwtService = jwtService;
        this.userDetailsService = userDetailsService;
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        String username = jwtService.getAuthUser(request);

        // 사용자가 존재하고, Spring Security Context에 인증 정보가 없다면
        if(username != null && SecurityContextHolder.getContext().getAuthentication() == null) {

            UserDetails userDetails = userDetailsService.loadUserByUsername(username);

            UsernamePasswordAuthenticationToken authentication =
                    new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
            authentication.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));

            SecurityContextHolder.getContext().setAuthentication(authentication);
        }
        filterChain.doFilter(request, response);
    }
}
```

- UsernamePasswordAuthenticationToken 생성자는 Spring Security에게 "인증이 완료된 사용자"의 정보를 등록하기 위해 사용된다.

- 이 생성자 안에 들어가는 세 개의 매개변수는 인증된 사용자의 **"신분증(Authentication)"**을 구성하는 3대 핵심 요소이다. ("누구인가?", "무엇으로 인증했는가?", "무엇을 할 수 있는가?")

- 생성자 매개변수 3개
    1. userDetails (The Principal: 주체)
        - 인증에 성공한 사용자 객체 그 자체이다. 이 객체 안에는 사용자의 ID, (암호화된) 패스워드, 권한, 계정 만료 여부 등 DB에서 가져온 모든 정보가 포함되어 있다.
    2. null (The Credentials: 자격 증명)
        - "무엇으로 인증했는가?" (The Password)
        - 원래 이 자리는 사용자가 로그인 시 입력한 '비밀번호' 같은 자격 증명을 넣는 곳이다. 이 코드는 이미 JWT 토큰 검증이 끝난 후이다. 즉, 인증이 완료되었기 때문에 더 이상 원본 비밀번호가 필요 없다. 보안상의 이유로, 인증이 완료된 '신분증' 객체에는 민감한 정보(비밀번호)를 즉시 null로 지워버리는 것이 원칙이다.
    3. userDetails.getAuthorities() (The Authorities: 권한)
        - "무엇을 할 수 있는가?" (The Roles/Permissions)
        - getAuthorities()는 userDetails 객체(DB에서 가져온)에 저장된 사용자의 권한 목록(예: ROLE_USER, ROLE_ADMIN)을 꺼낸다. 이 정보는 "인증(Authentication)" 이후의 "인가(Authorization)" 과정에서 사용된다. Spring Security는 이 목록을 보고 "이 사용자가 '관리자 페이지'에 접근할 수 있나?" (hasRole('ADMIN')) 같은 권한 검사를 수행한다.

### 스프링 시큐리티 vs. 필터

- Filter는 가장 기본적인 HTTP 요청 단위의 문지기이다.

  1. 요청이 컨트롤러로 들어가기 전에 검사할 수 있다.
  2. 인증/인가 로직을 직접 구현 가능
  3. 모든 로직을 직접 작성해야 함 (토큰 검증, 예외 처리, 사용자 세션 등)
     즉, 필터는 “이 요청을 통과시킬까, 막을까”만 판단하는 매우 저수준(low-level)의 기능이다.

- 스프링 시큐리티는 단순한 필터 한두 개가 아니라, 수십 개의 필터 + 인증/인가 관리 체계 + 세션/토큰 관리 + 암호화 + 예외 처리 + DSL 설정 시스템이 `모두 합쳐진 ‘보안 프레임워크’` 이다. 즉, “보안 전체를 체계적으로 다루는 프레임워크”인 것이다. 보통 프로젝트에서는 필터와 스프링 시큐리티 둘 다 함께 쓴다.

- 즉, 필터만으로도 보안은 가능하지만, `스프링 시큐리티는 그걸 체계적이고 확장 가능하게 만들어주는 ‘완성형 보안 프레임워크’` 이다.

## JWT

- JWT(JSON Web Token)은 당사자 간에 정보를 JSON 형태로 안전하게 전송하기 위한 토큰이다. JWT는 URL로 이용할 수 있는 문자열로만 구성돼있으며, 디지털 서명이 적용돼 있어 신뢰할 수 있다.

### JWT의 구조

- JWT는 점('.')으로 구분된 세 부분으로 구성된다. - 헤더(Header) - 내용(Payload) - 서명(Signature)
  따라서 JWT는 일반적으로 `xxxxx(헤더).yyyyy(내용).zzzzz(서명)`같은 형식을 띈다.

- 헤더
  - 검증과 관련된 내용을 담고있다.
- 내용
  - 토큰에 담는 정보를 포함한다.
  - 이곳에 포함된 속성들은 클레임(Claim)이라 하며, 크게 세가지로 분류된다.
    1. 등록된 클레임(Registered Claims)
       - 필수는 아니지만 토큰에 대한 정보를 담기위해 이미 이름이 정해져있는 클레임을 뜻한다.
    2. 공개 클레임(Public Claims)
    3. 비공개 클레임(Private Claims)
- 서명
  - 인코딩된 헤더, 인코딩된 내용, 비밀키, 헤더의 알고리즘 속성값을 가져와 생성된다. 서명은 토큰의 값들을 포함해서 암호화하기 때문에 메시지가 도중에 변경되지 않았는지 확인할 때 사용된다.

### JwtService

- jwt 토큰 생성

```java
package com.shoppinglist.shoppinglist2.security;

import io.jsonwebtoken.Jwts;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.http.HttpHeaders;
import org.springframework.stereotype.Component;

import javax.crypto.SecretKey;
import java.util.Date;

@Component
public class JwtService {
    static final long EXPIRATION_TIME = 86400000;
    static final String PREFIX = "Bearer ";
    private final SecretKey key = Jwts.SIG.HS256.key().build();

//    JWT 생성
    public String generateToken(String username) {
        String jwt = Jwts.builder()
                .subject(username)
                .expiration(new Date(System.currentTimeMillis() + EXPIRATION_TIME))
                .signWith(key)
                .compact();
        return jwt;
    }

//    요청 헤더에서 JWT를 파싱하여 사용자 이름(subject) 추출
    public String getAuthUser(HttpServletRequest request) {
        String token = request.getHeader(HttpHeaders.AUTHORIZATION);
        if(token != null && token.startsWith(PREFIX)) {
            try{
                String user = Jwts.parser()
                        .verifyWith(key) // 비밀 키로 검증
                        .build()
                        .parseSignedClaims(token.replace(PREFIX, "")) // 접두사 "Bearer " 제거
                        .getPayload()
                        .getSubject();

                if(user != null) {
                    return user;
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return null; // getAuthUser 메서드 호출했는데 user 안튀어나올때, null을 반환한다. -> 토큰이 없거나 유효하지 않음
    }
}

```

- generateToken()

```java
public String generateToken(String username) {
        String jwt = Jwts.builder()
                .subject(username)
                .expiration(new Date(System.currentTimeMillis() + EXPIRATION_TIME))
                .signWith(key)
                .compact();
        return jwt;
    }
```

- subject(username)
  이 메서드는 JWT의 '페이로드(Payload)' 부분에 **'sub' (Subject) 클레임(Claim)**을 설정한다.
  즉, 이 토큰이 누구에 관한 것인지를 나타낸다. 여기에 username을 넣으면, 나중에 이 토큰을 디코딩(해독)했을 때, 이 토큰이{username}이라는 사용자의 것이라고 식별할 수 있다.

- signWith(key)
  이 메서드는 JWT의 '서명(Signature)' 부분을 생성한다. 토큰이 위조되지 않았음을 증명하고, 누가 발급했는지 확인하는 데 사용된다. 제공된 key (비밀 키)를 사용하여, 앞서 만든 '헤더(Header)'와 '페이로드(Payload)'를 정해진 알고리즘(예: HS256)으로 암호화하여 서명 값을 만든다. 나중에 서버가 토큰을 받으면, 똑같은 key를 사용해서 서명을 검증한다. 만약 서명이 일치하지 않으면 (누군가 내용을 변경했거나, 키를 모르는 제3자가 토큰을 만들었다면) 그 토큰은 유효하지 않은 것으로 간주한다.

- compact()
  이 메서드는 빌더(Builder)를 통해 설정된 모든 정보(헤더, 페이로드, 서명)를 모아 최종적인 JWT 문자열을 생성한다.
  설정된 값들을 바탕으로 실제 토큰을 **'압축'하고 '직렬화'**한다. 그 결과 xxxxx.yyyyy.zzzzz와 같이 점(.)으로 구분된, Base64URL로 인코딩된 긴 문자열을 반환한다. 이 문자열이 바로 클라이언트에게 전달되는 최종 토큰이다.

- getAuthUser()

```java
 public String getAuthUser(HttpServletRequest request) {
        String token = request.getHeader(HttpHeaders.AUTHORIZATION);
        if(token != null && token.startsWith(PREFIX)) {
            try{
                String user = Jwts.parser()
                        .verifyWith(key) // 비밀 키로 검증
                        .build()
                        .parseSignedClaims(token.replace(PREFIX, "")) // 접두사 "Bearer " 제거
                        .getPayload()
                        .getSubject();

                if(user != null) {
                    return user;
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return null; // getAuthUser 메서드 호출했는데 user 안튀어나올때, null을 return : 토큰이 없거나 유효하지 않음
    }

```

### JwtAuthenticationFilter

- JWTAuthenticationFilter는 JWT 토큰으로 인증하고 SecurityContextHolder에 추가하는 필터를 설정하는 클래스이다.

```java
package com.shoppinglist.shoppinglist2.security;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;

// JwtService와 UserDetailsServiceImpl을 주입받을 것이다.
@RequiredArgsConstructor
public class JwtAuthenticationFilter extends OncePerRequestFilter {
    private final JwtService jwtService;
    private final UserDetailsServiceImpl userDetailsService;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
//        header에서 사용자 이름(username)을 추출
        String username = jwtService.getAuthUser(request);

//        사용자가 존재하고, Spring Security Context에 인증 정보가 없다면
        if(username != null && SecurityContextHolder.getContext().getAuthentication() == null) {
//            DB에서 user 정보 조회
            UserDetails userDetails = userDetailsService.loadUserByUsername(username);
//            토큰이 유효하면 인증 토큰을 생성하여 SecurityContext에 등록
//            잘 생각해보면 getAuthUser()에서 검증이 끝났다.
            UsernamePasswordAuthenticationToken authentication =
                    new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
            authentication.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
            SecurityContextHolder.getContext().setAuthentication(authentication);
        }
        filterChain.doFilter(request, response);
    }
}

```

## SecurityContext

1. SecurityContextHolder (SecurityContext를 담는 보관함)

- 특징
  - SecurityContextHolder는 이 보관함을 어떻게 저장하고 꺼낼지(전략)를 관리하는 유틸리티 클래스.
  - 가장 중요한 점은, 기본적으로 ThreadLocal 전략을 사용한다는 것이다.
    ThreadLocal이란? 현재 요청을 처리하는 스레드(Thread) 전용 저장소다. HTTP 요청이 들어오면 서버(톰캣 등)가 스레드를 하나 할당하는데, 그 요청이 끝날 때까지 SecurityContextHolder를 통해 저장된 정보는 오직 그 스레드 안에서만 접근할 수 있다. 그래서 다른 요청(다른 스레드)의 정보와 섞이지 않는다.

2. SecurityContext (Authentication 객체를 담는 상자)

- 특징
  - `인터페이스(interface)`. (기본 구현체는 SecurityContextImpl)
  - SecurityContextHolder라는 보관함에는 바로 이 SecurityContext '상자'가 들어간다. 이 상자의 유일한 임무는 Authentication 객체(신분증)를 보관하는 것이다. SecurityContext는 '락커룸 안에 넣는 손님의 개인 소지품 상자'이다.

3. Authentication (실제 인증 정보를 담고 있는 신분증 또는 출입증)

- 특징

  - `인터페이스(interface)`
  - 여기에는 사용자에 대한 핵심 정보가 모두 들어있다.

- Authentication의 메서드
  getPrincipal(): "누구인가?" (예: 사용자의 ID, 또는 UserDetails 객체 자체) // Principal : 본인
  getCredentials(): "무엇으로 인증했는가?" (예: 비밀번호. 인증이 완료된 후에는 보안을 위해 보통 null로 지운다.)
  getAuthorities(): "무엇을 할 수 있는가?" (예: ROLE_USER, ROLE_ADMIN 같은 권한 목록)

비유: Authentication은 '상자 안에 들어있는 손님의 신분증과 출입 카드'이다. 이 카드에는 이름(Principal)과 출입 가능 구역(Authorities)이 적혀 있다.

### 요약 및 흐름

이 세 가지 구성 요소를 하나로 합치면 다음과 같은 흐름이 된다.

1. 사용자가 로그인을 시도한다. (예: ID/PW 입력)

2. Spring Security가 이 정보를 바탕으로 Authentication 객체(미인증 상태의 신분증)를 만든다.

3. AuthenticationManager가 이 '신분증'이 진짜인지 확인(인증)한다.

4. 인증에 성공하면, Spring Security는 새로운 Authentication 객체(인증 완료 상태, 권한 정보 포함)를 생성한다.

5. 이 '인증된 신분증'(Authentication)을 '상자'(SecurityContext)에 넣는다.

6. 이 '상자'(SecurityContext)를 '현재 스레드 전용 보관함'(SecurityContextHolder)에 저장한다.

7. 이제 요청이 처리되는 동안, 애플리케이션의 어느 곳에서든 SecurityContextHolder를 통해 현재 사용자의 정보를 꺼내 쓸 수 있다.

## User

- User 클래스는 스프링 시큐리티의 구현체이다. 즉, User 클래스는 `UserDetails 인터페이스의 “구현체(implementation)”`이다.
- User 클래스는 스프링에서 제공하는 예제에 불과하다. 간단한 예제나 테스트용으로는 좋지만, 각 회사의 모든 비즈니스 정보(예: 포인트, 등급, 주소)를 담기엔 필드가 적합하지 않다.
  그래서 실제로는 User 클래스대신 각자의 사정에 맞는 클래스를 정의해서 그곳에 정보들을 담은 뒤 UserDetails를 implemets한다. -> 유연성 극대화
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

그래서 UserDetails 객체를 만드려면 별개의 수단이 필요한데, 우리가 흔히 쓰는 건 User 클래스의 빌더이다.

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

    public static UserBuilder builder() {
        return new UserBuilder();
    }

    // 빌더 클래스가 User 내부에 정의되어 있음
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

## UserDetailsService

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
