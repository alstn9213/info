def calc():
  a=3
  b=5
  def mul_add(x):
    return a*x+b
  return mul_add

c = calc()

print(c(1), c(2), c(3), c(4), c(5))

def calc2():
  a=3
  b=5
  return lambda x: a*x+b

c2 = calc2()
print(c2(1), c2(2), c2(3), c2(4), c2(5))