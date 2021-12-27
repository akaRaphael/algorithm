# 문자열 정렬하기
# https://programmers.co.kr/learn/courses/4008/lessons/13326

s, n = input().strip().split(' ')
n = int(n)

# 내가 짠 코드 
empty = n - len(s)
space = empty // 2
left = 0
right = 0
for i in range(3):
  left = space * i
  right = empty - left
  print(" " * left + s + " " * right)
    
# pythonic한 코드 
# ljust(문자열 전체 길이): 좌측정렬
# center(): 가운데정렬 
# rjust(): 우측정렬

print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))