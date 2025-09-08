# 제너레이터는 이터레이터를 생성해주는 함수다.
# 이터레이터는 클래스에 __iter__, __next__, __getitem__ 등의 메서드를 구현해야하지만 제너레이터는 함수 안에 yield 키워드만 사용하면 끝이다.

# 함수안에서 yeild를 사용하면 함수는 제너레이터가 된다.
# yeild에는 값(변수)를 지정한다.

def number_generator():
  yield 0
  yield 1
  yield 2

for i in number_generator():
  print(i)

# 제너레이터 객체 생성
g = number_generator()

# 제너레이터 객체에서 __next__()메서드를 호출할 때마다 함수안의 yield를 실행하며 yield에서 값을 발생시킨다.
print(g.__next__())
print(g.__next__())
print(g.__next__())

# 인덱스를 벗어날 경우 예외발생
# print(g.__next__()) # 에러
