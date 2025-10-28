# security

## JwtService
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
        return null; // getAuthUser 메서드 호출했는데 user 안튀어나올때, null을 return : 토큰이 없거나 유효하지 않음
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

## JwtAuthenticationFilter
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