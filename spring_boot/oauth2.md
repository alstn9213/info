# Oauth2

## 네이버 Oauth2

1. application.properties 설정

1) Registration (우리 앱 등록 정보)

   - 이 설정들은 Spring Boot에게 "우리 앱은 네이버에 이렇게 등록되어 있다"고 알려주는 정보이다.

```ini
spring.security.oauth2.client.registration.naver.client-id=my_id
spring.security.oauth2.client.registration.naver.client-secret=my_secret_key

# 네이버가 사용자를 다시 돌려보낼 우리 서버의 주소(콜백 URL)이다.
# 사용자가 네이버 로그인에 성공하면, 네이버 서버가 브라우저를 이 주소로 리디렉션시킨다. 이때 code라는 임시 인가 코드를 함께 실어 보낸다.
흐름: 2단계에서 사용자가 네이버 로그인에 성공하면, 네이버 서버가 브라우저를 이 주소로 리디렉션시킵니다. 이때 code라는 임시 인가 코드를 함께 실어 보냅니다.
spring.security.oauth2.client.registration.naver.redirect-uri=http://localhost:8080/login/oauth2/code/naver

# OAuth2의 여러 인증 방식 중 어떤 방식을 사용할지 명시한다. authorization_code (인가 코드) 방식은 "로그인 -> code 발급 -> code를 Access Token으로 교환"하는 가장 표준적이고 안전한 방식이다.
spring.security.oauth2.client.registration.naver.authorization-grant-type=authorization_code


# 우리가 네이버에게 어떤 정보에 접근하도록 사용자에게 허락을 요청할 것인지를 명시하는 목록이다.
spring.security.oauth2.client.registration.naver.scope=name,email
```

2. Provider(네이버 서버 정보)

   - 이 설정들은 Spring Boot에게 "네이버 서버와 통신하려면 이 주소(API 엔드포인트)로 요청을 보내야 한다"고 알려주는 주소록이다.

```ini
#사용자가 로그인하고 '동의' 버튼을 누를 페이지의 주소
# 네이버가 제공하는 고유한 인증 페이지 주소이기때문에 변경 불가
spring.security.oauth2.client.provider.naver.authorization-uri=https://nid.naver.com/oauth2.0/authorize

#앞서 받은 code(인가 코드)를 주고 Access Token(접근 토큰)으로 교환할 때 사용할 주소.
# 네이버의 토큰 발급 API 주소이기 때문에 변경 불가
spring.security.oauth2.client.provider.naver.token-uri=https://nid.naver.com/oauth2.0/token

#Access Token을 가지고 실제 사용자 정보(이름, 이메일)를 조회할 때 사용할 주소.
# 네이버의 사용자 정보 조회 API 주소이기 때문에 변경불가
spring.security.oauth2.client.provider.naver.user-info-uri=https://openapi.naver.com/v1/nid/me

#위의 user-info-uri에서 받은 JSON 데이터의 구조를 Spring Security에게 알려준다."
# 네이버의 API 응답 형식이 response 키를 사용하도록 강제하기때문에 변경 불가
# user-name-attribute는 Spring Security가 우리(개발자)에게 묻는 질문.
# 네이버에서 사용자 정보를 JSON으로 받아왔을 때, 실제 사용자 정보가 어떤 키(key) 값 안에 들어있는지 알려줘야하고 그 **'최상위 키'**는 response다.
spring.security.oauth2.client.provider.naver.user-name-attribute=response
```
