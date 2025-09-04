# 정적 메서드는 @staitcmethod를 붙여 만든다.
# 정적 메서드는 객체를 만들지 않아도 사용할 수 있다.
# 정적 메서드는 외부 상태에 영향을 끼치지 않는 순수 함수를 만들때 사용한다. 순수함수는 부수효과가 없고 입력값이 같으면 언제난 같은 출력값을 반환한다.
class Calc:
  @staticmethod
  def add(a, b):
    print(a + b)
  @staticmethod
  def mul(a, b):
    print(a * b)

Calc.add(10,20)
Calc.mul(10,20)