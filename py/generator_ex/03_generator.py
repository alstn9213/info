# range()처럼 동작하는 제너레이터

def number_generator(stop):
  n = 0
  while n < stop:
    yield n
    n += 1

# for i in number_generator(3):
#   print(i)

g = number_generator(3)
next(g)
next(g)
next(g)

#  yield값을 대문자로 변환
# def upper_generator(x):
#   for i in x:
#     yield i.upper()

