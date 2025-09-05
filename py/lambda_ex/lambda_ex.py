# 람다 표현식
# 함수를 간편하게 작성가능
# 다른 함수의 인수로 넣을 때 주로 사용

# 람다 표현식을 정의만 한 상태에서는 호출할 수없다.
print(lambda x: x + 10) # <function <lambda> at 0x0000022D02CA3BA0>

# 람다 표현식을 사용하려면 변수에 람다 표현식을 대입해야한다.
plus_ten_lambda = lambda x: x + 10
print(plus_ten_lambda(1))

# 람다 표현식을 변수에 할당하지않고 람다 표현식 자체를 바로 호출하는 방법
(lambda x: x+10)(1) # 11

# 람다 표현식 안에서는 새 변수를 만들 수 없다.
# (lambda x: y = 10; x + y)(1) # 오류 발생

# 람다 표현식 바깥에 있는 변수는 사용할 수 있다.
y = 10
(lambda x: x+y)(1) # 11

def plus_ten(x):
  return x + 10

# map
# 함수로 만든 map
# list_ex = list(map(plus_ten, [1,2,3]))
# print(list_ex) # [11, 12, 13]

# 람다 표현식으로 만든 amp
list_ex = list(map(lambda x: x + 10, [1,2,3]))
print(list_ex) # [11, 12, 13]

a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))
# [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]