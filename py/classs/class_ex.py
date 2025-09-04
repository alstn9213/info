class Person:
  def greeting(self):
    print('Hello')
  
# 파이썬에서 클래스로 객체를 만들때 자바와 달리 new 키워드가 필요없다.
james = Person()

james.greeting() 
# Hello

# 클래스에서 속성을 만들때는 __init__ 메서드안에서 self.속성에 값을 할당한다.
# 이는 마치 자바의 생성자와 같은 역할을 한다.
class Person2:
  def __init__(self):
    self.hello = 'hi'
  def greeting(self):
    print(self.hello)

John = Person2()
John.greeting()

# 변수도 할당가능
class Person3:
  def __init__(self, name, age, address):
    self.hello = 'hello'
    self.name = name
    self.age = age
    self.address = address
  def greeting(self):
    print('{0} is {1}'.format(self.hello, self.name))

maria = Person3('maria', 20, 'seoul')
maria.greeting()

print('name', maria.name)
print('age', maria.age)
print('address', maria.address)

    

  