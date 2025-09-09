lax_coordinates = (33.9425, -118.408056)

# 언패킹
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

print(divmod(20, 8))
t = (20, 8)
divmod(*t)
quotient, remainder = divmod(*t)
print(quotient, remainder)

# 매개변수를 별표 인수로 정의해서 임의의 초과 인수를 가져올 수 있다.
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)

# 병렬할당할 때 별표는 단 하나의 변수에만 적용할 수 있다. 
# 하지만 변수 위치에는 제한이 없다.
a, *body, c, d = range(5)
print(a, body, c, d)
*head, b, c, d = range(5)
print(head, b, c, d)


def fun(a, b, c, d, *rest):
  return a, b, c, d, rest
print(fun(*[1,2], 3, *range(4,7)))
