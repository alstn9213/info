# 파일 처리

# 파일에 문자열을 써서 파일을 만들기
file = open('hello.txt', 'w') # 두번째 인수로 w
file.write('Hello, world!') # write 메서드 사용
file.close()

# 파일에서 문자열 읽기
file = open('hello.txt', 'r') # 두번째 인수로 r
s = file.read() # read()메서드 사용
print(s)
file.close()

# 자동으로 파일 객체 닫기
# with as를 쓰면 close() 메서드를 쓰지않아도 된다.
with open('hello.txt', 'r') as file:
  s = file.read()
  print(s)

# 반복문으로 문자열 여러 줄을 파일에 쓰기
with open('hello.txt', 'w') as file:
  for i in range(3):
    file.write('Hello, world! {0}\n'.format(i))

# writelines() 메서드로 리스트의 문자열 요소를 파일에 쓰기
lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
with open('hello.txt', 'w') as file:
  file.writelines(lines)

# readlines() 메서드로 파일의 내용을 한 줄씩 리스트로 가져오기
with open('hello.txt', 'r') as file:
  lines = file.readlines()
  print(lines)

# readline()메서드로 파일의 내용을 한줄씩 읽기
with open('hello.txt', 'r') as file:
  line = None
  while line != '':
    line = file.readline()
    print(line.strip('\n'))

# for문으로 한줄씩 읽기
with open('hello.txt', 'r') as file:
  for line in file:
    print(line.strip('\n'))