# yield from

# 값을 바깥으로 여러번 전달할 때, 반복문으로 yield 값을 받아오기보다는 yield from을 사용하면 간편하다.

# 기존 방식
# def number_generator():
#   x = [1,2,3]
#   for i in x:
#     yield i

# for i in number_generator():
#   print(i)

# yield from 사용
def number_generator():
  x = [1,2,3]
  yield from x

for i in number_generator():
  print(i)


# yield from에 제너레이터 객체 지정
def number_generator2(stop):
  n = 0
  while n < stop:
    yield n
    n += 1

def three_generator():
# 제너레이터 객체 지정
  yield from number_generator2(3)

for i in three_generator():
  print(i)