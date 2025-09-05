def number_generator():
  yield 0
  yield 1
  yield 2

g = number_generator()
a = next(g)
print(a)

b = next(g)
print(b)

c = next(g)
print(c)

def one_generator():
  yield 1
  return 'return value'

try:
  g = one_generator()
  next(g)
  next(g)
except StopIteration as e:
  print(e)