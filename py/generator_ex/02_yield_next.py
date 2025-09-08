def number_generator():
  yield 0
  yield 1
  yield 2

g = number_generator()

# next(g)를 호출하면 제너레이터 안의 yield 0 이 실행되어 숫자 0을 전달한뒤 바깥의 코드가 실행되도록 양보한다.
a = next(g) 
print(a)

# a가 출력됐으니 다시 제너레이터 안의 코드를 실행한다. 이때는 yield 1이 실행되고 숫자 1을 발생시켜서 바깥으로 전달.
b = next(g)
print(b)

c = next(g)
print(c)

# 제너레이턴는 함수를 끝내지 않은 상태에서 yield를 사용하여 값을 바깥으로 전달할 수 있다.