# 파일 사용하기

```py
# 파이썬에서 바로 파일 생성
file = open('hello.txt', 'w')
file.write('Hello World!')
file.close()

# 저장된 파일 읽기
file = open('hello.txt', 'r')
s = file.read()
print(s)
file.close()

# close로 객체를 닫지않아도 되는 방식
with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)

# 반복문으로 문자열 여러 줄을 파일에 쓰기
with open('hello.txt', 'w') as file:
  for i in range(3):
    file.write('Hello, world {0}\n'.format(i))

# 리스트에 들어있는 문자열을 파일에 쓰는 방식

lines = ['안녕하세요\n','파이썬\n','코인도장입니다.\n']
with open('hello.txt', 'w') as file:
  file.writelines(lines)

```

