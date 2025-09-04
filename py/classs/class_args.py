class Person:
  def __init__(self, *args):
    self.name = args[0]
    self.age = args[1]
    self.address = args[2]

maria = Person(*['maria', 20, 'seoul'])

class Person2:
  pass
john = Person2()
john.name = 'john'
john.name
