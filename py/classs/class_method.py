# 클래스 메서드는 인스턴스 없이 호출할 수 있다는 점은 정적메서드와 같다.
# 하지만 클래스메서드는 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야할 때 사용한다.
class Person:
  count = 0
  def __init__(self):
    Person.count += 1
  @classmethod
  def print_count(cls):
    print('{0} is created'.format(cls.count))

james = Person()
maria = Person()

Person.print_count()