# 예외처리
# - 예외란 코드를 실행하는 중에 발생하는 에러
# - 예외처리는 예외가 발생했을 때도 스크립트 실행을 중단하지 않고 계속 실행하게 해준다.

# try:
#   x = int(input('나눌 숫자를 입력하세요: '))
#   y = 10 / x
#   print(y)
# except: 
#   print('예외발생')

# 특정 예외만 처리
# try:
#   x = 3
#   if x % 3 != 0:
#     raise Exception('3의 배수가 아닙니다.') # 예외가 발생해서 아래의 코드가 실행되지않음
#     print(x) 
# except Exception as e: 
#   print('예외발생', e)

y = [10, 20, 30]
try:
  index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ')).split()
  print(y[index]/x)
except ZeroDivisionError: # 숫자를 0으로 나눠서 에러 발생하는 경우
  print('숫자를 0으로 나눌 수 없습니다.')
except IndexError: # 범위를 벗어난 인덱스에 접근하여 에러가 발생하는 경우
  print('잘못된 인덱스입니다.')

# def three_multiple():
#   x = 5
#   if x % 3 != 0:
#     raise Exception('3의 배수가 아닙니다.')
#   print(x)

# try:
#   three_multiple()
# except Exception as e:
#   print('예외가 발생했습니다.', e)


# raise만 사용하면 같은 예외를 상위 코드 블록으로 넘긴다.
def three_multiple():
  try:
    x = 5
    if x % 3 != 0:
      raise Exception('3의 배수가 아닙니다.') # 2
    print(x)
  except Exception as e:
    print('three_multiple 함수에서 예외가 발생했습니다.', e) # 1
    raise # 3 예외를 상위 코드블록으로 넘긴다

try:
  three_multiple()
except Exception as e:
  print('스크립트 파일에서 예외가 발생했습니다.', e) # 4
# three_multiple 함수에서 예외가 발생했습니다. 3의 배수가 아닙니다. 스크립트 파일에서 예외가 발생했습니다. 3의 배수가 아닙니다. 

# raise에 다른 예외를 지정하고 에러메시지를 넣을 수도 있다.
def three_multiple():
  try:
    x = 5
    if x % 3 != 0:
      raise Exception('3의 배수가 아닙니다.') 
    print(x)
  except Exception as e:
    print('three_multiple 함수에서 예외가 발생했습니다.', e) 
    raise RuntimeError('three_multiple 함수에서 예외가 발생했습니다.') # 다른 예외 지정

try:
  three_multiple()
except Exception as e:
  print('스크립트 파일에서 예외가 발생했습니다.', e) 