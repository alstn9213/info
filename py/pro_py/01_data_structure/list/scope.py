# 지능형 리스트

x = 'ABC'

# ord() 함수는 하나의 문자를 인자로 받아 해당 문자의 유니코드 포인트를 반환
codes = [ord(x) for x in x]
print(x)
print(codes)

# := : 바다코끼리 연산자와 함께 할당된 변수는 함수의 지역변수와 달리 지능형 표현식이 반환된 뒤에도 여전히 접근할 수 있다.
codes = [last := ord(c) for c in x]
print(last)
# print(c) 에러

symbols = '$&@#'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

