# JpaRepository
- 우리는 JpaRepository 인터페이스를 상속받은 인터페이스를 사용해, 데이터베이스에 엔티티 객체를 저장하거나 조회, 수정, 삭제한다. 
- JpaRepository 인터페이스를 상속받는 인터페이스를 정의하면 findById 같은 메서드를 사용할 수 있다.
그런데 인터페이스는 추상 메서드만 정의하고 구체적인 작동방식은 정의되지 않았을 텐데 어째서 findById같은 메서드를 사용할수있는 걸까?

```java
public interface UserRepository extends JpaRepository<AppUser, Long> {
}

```
- 사실 위의 인터페이스에는 findById, save, delete 같은 메서드의 정의만 있고 구현은 없다. 그럼에도 저런 메서드들을 사용할 수 있는 것은 우리가 만든 껍데기 인터페이스에 Spring이 구현체를 런타임에 만들어 주기때문이다. 구체적으로는 Spring Data JPA의 프록시 생성기가 구현체를 만드는데, `@SpringBootApplication` 안에 포함되어 있는 `@EnableJpaRepositories`가 JpaRepository를 상속받은 모든 인터페이스를 스캔하고, 인터페이스마다 프록시(Proxy) 객체를 자동 생성한다. 이 프록시 객체가 내부적으로 EntityManager를 사용해서 실제 SQL을 수행한다.
- 즉, 우리가 호출하는 건 진짜 구현체가 아니며, "Spring이 자동으로 만들어준 가짜 객체(Proxy)"를 호출하는 것이며 이들이 실제 JPA 코드(EntityManager 등)를 대신 실행한다. 컴파일러는 구현되지않은 추상 메서드가 있더라도 실제 구현체를 “스프링이 런타임에 만들어줄 것”을 전제로 하기 때문에 오류를 발생시키지않는다. 
- 예를 들어 findById(1L)를 호출하면, Spring Data JPA는 다음과 같이 처리한다:
```java
@Override
public Optional<AppUser> findById(Long id) {
    return entityManager.find(AppUser.class, id);
}

```
이 구현을 우리가 직접 쓰지 않아도, 스프링이 자동으로 제공한다.

## JpaRepository 커스텀 메서드
- JPA는 특정 컬럼을 조건으로 검색하기위해 'findBy + 컬럼이름'과 같은 명명 규칙을 지원한다. 예를 들어 다음 같은 커스텀 메서드를 선언해도
```java
List<AppUser> findByUsername(String username);
 
```
Spring은 메서드 이름을 분석해서 자동으로 JPQL을 만들어낸다.
```sql
SELECT u FROM AppUser u WHERE u.username = :username
```
즉, findBy + 필드명 패턴을 읽어내서 쿼리를 구성하는 “메서드 이름 파서(parser)”가 내장되어 있다.

- 아이디를 검색하는 것이 아니라면 여러 개가 조회될 수 있으므로 List타입으로 반환받도록 정의해야한다.

- 두가지 이상의 조건을 검색하려면 검색 조건에 사용하려는 컬럼이름을 AND 또는 OR로 연결해 복수의 컬럼으로 검색할 수 있다.
```java
 public interface MemberRepository extends JpaRepository<Member, Long> {
    List<Member> findByAndEmail(String name, String email);
}
```