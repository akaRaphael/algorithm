# 백준 단계별 풀이 5단계
# https://www.acmicpc.net/problem/4344

import sys

caseNum = int(input())
for _ in range(caseNum):
  arr = list(map(int, sys.stdin.readline().split()))
  average = sum(arr[1:]) / arr[0]
  count = 0
  for score in arr[1:]:
    if score > average:
      count += 1
  result = count / arr[0] * 100
  print(f'{result:.3f}%')