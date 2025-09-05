# map 

# 형식
# map(바꾸고싶은자료형, 반복가능객체)


a = [1.2, 2.5, 3.7, 4.6]

# 리스트의 모든 요소를 정수로 변환할 때 for문을 쓰는 것은 번거롭다.
# for i in range(len(a)):
#   a[i] = int(a[i])

# print(a) # [1, 2, 3, 4]

# 그래서 map을 쓴다.
a = list(map(int, a))
print(a) # [1, 2, 3, 4]


# 0~9까지의 숫자를 문자열로 바꾸는 예제
# a = list(map(str, range(10)))
# print(a)

a = map(int, input().split())