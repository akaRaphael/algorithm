# 백준 단계별 풀이 5단계
# https://www.acmicpc.net/problem/8958

import sys

n = int(input())
for _ in range(n):
  result = 0
  score = 0
  arr = sys.stdin.readline().strip()
  for data in arr:
    if(data == 'O'):
      score += 1
      result += score
    else:
      score = 0
  print(result)
  
