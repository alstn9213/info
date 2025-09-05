# 반복 가능객체와 이터레이터
# 이터레이터는 값을 하나씩 꺼낼수 있는 객체이다.

it = [1,2,3].__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())

it = range(3).__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())

class Counter:
  def __init__(self, stop):
    self.current = 0
    self.stop = stop

  def __iter__(self):
    return self

  def __next__(self):
    if self.current < self.stop:
      r = self.current 
      self.current += 1
      return r
    else:
      raise StopIteration
for i in Counter(3):
  print(i, end=' ')

