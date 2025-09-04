# 클래스 속성은 __init__ 을 사용하지않고 클래스에 바로 속성을 만든다.
# 클래스 속성은 클래스에 속해있기 때문에 모든 인스턴스에서 공유한다.
class Person:
  bag = []
  def put_bag(self, stuff):
    self.bag.append(stuff)

james = Person()
james.put_bag('book')
maria = Person()
maria.put_bag('key')
# 인스턴스에 개별적으로 값을 넣어도 모든 인스턴스가 값을 공유한다.
print(james.bag) # ['book', 'key']
print(maria.bag) # ['book', 'key']

# self는 현재 인스턴스를 의미하므로 클래스 속성을 지칭하기에는 의미가 모호하다.
# 그래서 클래스 속성에 접근할 때는 클래스 이름으로 접근하면 코드가 명확해진다.
class Person2:
  bag = []
  def put_bag(self, stuff):
    Person2.bag.append(stuff)

print(Person2.bag)

# 그러므로 모든 인스턴스가 값을 공유해야할 때는 클래스 속성, 인스턴스 별로 값을 정해줄 때는 인스턴스 속성을 쓴다.