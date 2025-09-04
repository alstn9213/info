# global 키워드를 사용할 경우 함수 안에서도 전역변수를 사용할 수 있다.

x = 10
def foo():
  global x
  x = 20
  print(x)

foo()
print(x)

# locals() 함수를 사용할 경우 현재의 네임스페이스를 딕셔너리형태로 출력할 수 있다.

def foo2():
  x = 10
  print(locals())

foo2() # {'x': 10}

# nonlocal 키워드를 사용할 경우 외부함수에 정의된 변수를 내부 함수에서 사용할 수 있다.

# def A():
#   x = 10
#   def B():
#     nonlocal x
#     x = 20
#   B()
#   print(x)

# A()

#  nonlocal은 현재 함수의 바깥쪽에 있는 지역 변수를 찾을 때 가장 가까운 함수부터 먼저 찾는다.
def A():
  x = 10
  y = 100
  def B():
    x=20
    def C():
      nonlocal x # B함수에 정의된 x=20을 사용한다.
      nonlocal y # A함수에 정의된 y=100을 사용한다.
      x = x + 30
      y = y + 300
      print(x)
      print(y)
    C() # 50
  B() # 400

A()

