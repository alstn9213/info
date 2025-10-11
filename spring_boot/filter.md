# AccessKeyFilter
- RESTful API는 URL만 알면 누구나 API를 호출해 회원정보를 생성하거나 특정한 회원이 작성한 게시글을 조회할 수 있다. 허가받은 클라이언트만 사용하도록하려면 스프링부트에서 제공하는 필터 기능을 사용하면 HTTP 헤더에 포함된 엑세스 키를 컨트롤러 앞단에서 검증할 수 있다. 즉, 엑세스 키를 검증하는 필터를 작성해 컨트롤러 앞 단에 배치함으로써 정상적인 엑세스키가 포함된 API 호출에 대해서만 컨트롤러에게 전달하고, 엑세스 키가 헤더에 포함되어 있지 않거나 엑세스키가 정상이 아닌 경우, 필터에서 바로 클라이언트로 401 Unauthorized 오류를 반환하도록 구현하면 된다.

-  웹 필터는 일반적으로 `OncePerRequestFilter` 를 상속받아 작성하는데, 이 경우 한번의 요청에 대해 한번만 필터를 거치도록한다. 실제 필터를 구현하기 위해 Filter 인터페이스를 구현하는 대신 OncePerRequestFilter를 상속받았으므로, 필터는 doFilter()대신 doFilterInternal()을 오버라이드해 작성한다. 

```java
package com.example.demo2.filter;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebFilter;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;

@WebFilter(urlPatterns = "/api/*")
@Slf4j
public class AccessKeyFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        log.info("AccessKeyFilter.doFilterInternal() begins");
        String authorization = request.getHeader("Authorization");
        if(authorization != null && authorization.startsWith("Bearer")) {
            String token = authorization.replace("Bearer", "").trim();
            if("hanbit-access-key".equals(token)) {
                filterChain.doFilter(request, response);
                log.info("AccessKeyFilter.doFilterInternal() returns");
                return;
            }
        }
        response.setStatus(HttpStatus.UNAUTHORIZED.value());
        log.info("AccessKeyFilter.doFilterInternal() returns Unauthorized");
    }
}
```
전달된 HttpServletRequest 파라미터에서 Authorization 헤더를 구한 후 Bearer를 제거한 엑세스 키가 'hanbit-access-key' 인지 검증한 다음, 정상적인 경우 다음 단계로 진행하고 아니면 인증 오류 401 Unauthorized를 반환한다. 그리고 `request.getHeader("Authorization");`에서 말하는 헤더는 HTTP 요청(Request)의 헤더(Header) 중에서 "Authorization" 이라는 이름을 가진 헤더 값을 가져오는 것이다.

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
    Authorization: Bearer <token>에서 "이 요청을 보낸 사람은 <token> 을 가지고 있으므로, 그 토큰이 유효하다면 접근을 허락해달라"라는 뜻이다. 
    - Bearer 토큰은 `“토큰을 소지하는 것만으로 인증이 완료되는 방식”`이다. 즉, 서버는 토큰을 받은 요청이 오면 토큰이 유효한지 검사하고 토큰이 유효하다면 그 사람은 인증된 것으로 간주한다.
 

## 스프링 시큐리티 vs. 필터
- Filter는 가장 기본적인 HTTP 요청 단위의 문지기이다. 
  1. 요청이 컨트롤러로 들어가기 전 에 검사할 수 있음
  2. 인증/인가 로직을 직접 구현 가능
  3. 모든 로직을 직접 작성해야 함 (토큰 검증, 예외 처리, 사용자 세션 등)
즉, 필터는 “이 요청을 통과시킬까, 막을까”만 판단하는 매우 저수준(low-level)의 기능이다.

- 스프링 시큐리티는 단순한 필터 한두 개가 아니라, 수십 개의 필터 + 인증/인가 관리 체계 + 세션/토큰 관리 + 암호화 + 예외 처리 + DSL 설정 시스템이 `모두 합쳐진 ‘보안 프레임워크’` 이다. 즉, “보안 전체를 체계적으로 다루는 프레임워크”. 보통 프로젝트에서는 필터와 스프링 시큐리티 둘 다 함께 쓴다.

- 즉, 필터만으로도 보안은 가능하지만, `스프링 시큐리티는 그걸 체계적이고 확장 가능하게 만들어주는 ‘완성형 보안 프레임워크’` 이다.