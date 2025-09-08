# 함수 안에서 전역 변수를 만들려면 global 키워드를 사용해야한다.

x = 10
def foo():
  global x
  x = 20
  print(x)

foo()
print(x)

# 클로저 사용하기
def calc():
  a = 3
  b = 5
  def mul_add(x):
    return a * x + b # 함수 바깥에 있는 지역변수 a, b를 사용
  return mul_add # mul_add함수를 반환

c = calc() # 이 시점에서 함수 calc는 끝났는데
print(c(1),c(2),c(3),c(4),c(5)) # c는 calc의 지역변수 a, b를 사용해서 계산한다.
# 이렇게 함수를 둘러싼 환경을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용하는 함수를 클로저라고 한다.

