# Gson
개발자들은 Gson 라이브러리를 만들때 클래스 구조를 크게 두가지 역할로 나눠 설계했다.

1) 데이터 모델 계층: JsonObject, JsonArray, JsonPrimitive, JsonNull
→ JSON 데이터를 자바에서 직접 다룰 수 있게 해주는 계층

2) 처리 계층: Gson
→ JSON과 자바 객체/문자열 간의 변환을 담당하는 계층

이렇게 역할을 둘로 분리하면 데이터 모델(JsonObject)을 가볍고 단순하게 유지할 수 있다는 이점이 생긴다. 즉, 데이터 모델이 그 자체의 역할에 집중할 수 있게 된 것이다. 그 덕에 JsonObject 클래스는 속성 추가(addProperty), 속성 읽기(get), 속성 존재 여부 확인(has)처럼 순수하게 데이터 모델만을 위한 메서드를 가진다. 만약 여기에 JsonObject를 다른 타입으로 변환하는 메서드까지 추가된다면 데이터 모델의 구조를 다룬다는 의미가 옅어질 것이다.
또한 변환 로직(Gson)을 별개의 영역으로 지정함으로써 변환 로직이 독립적으로 발전 가능할 수 있는 여지도 남겨 두었다. (예: pretty printing, custom serializer, type adapter 등)

## JsonObject
데이터 모델 계층에 포함된 JsonObject는 자바에서 JSON을 편하게 다루려고 자바가 JSON의 구조를 모방해서 자바 나름대로 만든 자료구조이다. 이는 JsonObject 그 자체로는 JSON이 될 수 없다는 뜻이다. 즉, JsonObject를 JSON의 형태로 바꾸는 작업이 따로 필요하다. JSON은 String타입이라 JsonObject를 String으로 변환해야하는데 이때 필요한 것이 Gson클래스이다.

## Gson
타입 변환을 책임지는 유틸리티 클래스다. 변환가능한 예시는 다음과 같다.

JsonObject ↔ String (텍스트)

자바 클래스 ↔ String (텍스트)

JsonObject ↔ 자바 클래스

```java
import com.google.gson.Gson;
import com.google.gson.JsonObject;

public class JsonTest {
    public static void main(String[] args) {
        JsonObject jsonObject1 = new JsonObject();
        Gson gson = new Gson();
        String jsonData = gson.toJson(jsonObject1); // JsonObject를 String타입으로 변환
        JsonObject jsonObject2 = gson.fromJson(jsonData, JsonObject.class); // String타입을 JsonObject로 변환
        System.out.println(jsonObject2);
    }
}
```