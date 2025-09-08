# coroutine
# 함수가 종료되지 않은 상태에서 메인 루틴의 코드를 실행한 뒤 다시 돌아와서 코루틴의 코드를 실행한다.
# 일반 함수를 호출하면 코드를 한번만 실행할 수 있지만 코루틴은 코드를 여러번 실행할 수 있다.
# 코루틴은 진입점이 여러 개인 함수이다.

def number_coroutine():
  while True: # 코루틴을 계속 유지하기 위해 무한 루프 사용
    x = (yield) # 코루틴 바깥에서 값을 받아옴
    print(x)

co = number_coroutine()

next(co) # 코루틴 안의 yield까지 코드 실행
co.send(1)
co.send(2)
co.send(3)

# 코루틴에서 바깥으로 값을 전달
def sum_coroutine():
  total = 0
  while True:
    x = (yield total)
    total += x

co = sum_coroutine()

print(next(co))
print(co.send(1))
print(co.send(2))
print(co.send(3))

# 코루틴 강제 종료 close()
def number_coroutine2():
  while True:
    x = (yield)
    print(x, end=' ')

co = number_coroutine2()

next(co)

for i in range(20):
  co.send(i)

co.close()