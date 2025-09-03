# def print_numbers(*args):
#   for arg in args:
#     print(arg)

# print_numbers(10)
# print_numbers(10, 20, 30, 40)

# x = [10]
# print_numbers(*x)
# y = [10, 20, 30, 40]
# print_numbers(*y)

def print_numbers(a, *args):
  print(a)
  print(args)

print_numbers(1)

print_numbers(1,10,20)

print_numbers(*[10, 20, 30])
