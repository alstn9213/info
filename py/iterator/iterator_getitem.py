# 인데스로 접근하는 이터레이터

class Counter:
  def __init__(self, stop):
    self.stop = stop

  def __getitem__(self, index):
    if index < self.stop:
      return index
    else:
      raise IndexError
    
print(Counter(3)[0])
print(Counter(3)[1])
print(Counter(3)[2])

for i in Counter(3):
    print(i, end=' ')