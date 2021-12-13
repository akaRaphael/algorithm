# 파이썬 50제 (1 ~ 50) - 주사위 게임
# https://www.acmicpc.net/problem/2476

t = int(input())
result = 0 
temp = 0
for _ in range(t):
  a, b, c = map(int, input().split())
  same = 0
  count = 0
  if a == b == c:
    count = 2
    same = a
  elif a == b:
    count = 1
    same = a
  elif b == c:
    count = 1
    same = b
  elif a == c:
    count = 1
    same = a
  
  if count == 2:
    temp = 10000 + same * 1000
  elif count == 1:
    temp = 1000 + same * 100
  else:
    temp = max(a, b, c) * 100
  
  if temp >= result:
    result = temp

print(result)