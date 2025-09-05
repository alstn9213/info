# filter 
# filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데, filter에 지정한 함수의 반환값이 True일 때만 해당 요소를 가져온다.

def f(x):
  return x > 5 and x < 10

a = [8,3,2,10,15,7,1,9,0,11]

# filter안에 함수 f를 넗고 f의 조건에 따라 a의 요소들을 반환한다.
print(list(filter(f,a))) # [8,7,9]