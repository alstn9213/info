# 언패킹
리스트나 튜플앞에 *를 붙이면 변수들이 풀려난다.
```py
def print_numbers(a,b,c):
  print(a)  
  print(b)
  print(c)

x = [10, 20, 30]

print_numbers(*x)
```

