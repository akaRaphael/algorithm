# 백준 단계별 풀이 12단계 - 수 정렬하기 
# https://www.acmicpc.net/problem/2750

# 파이썬 정렬 라이브러리를 사용하면 
t = int(input())
result = [] 
for _ in range(t):
  result.append(int(input()))

result.sort()
for data in result:
  print(data)

from typing import list