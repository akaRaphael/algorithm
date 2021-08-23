# 백준 단계별 풀이 12단계 - 수 정렬하기 
# https://www.acmicpc.net/problem/2750

# 버블정렬을 사용해서 풀어보자
from typing import List
from sys import stdin

input = stdin.readline

def bubble_sort (case: List[int]) -> List[int]:
  for idx in range(len(case) - 1):
    for j in range(len(case) - idx - 1):
      if case[j] > case[j + 1]:
        case[j], case[j + 1] = case[j + 1], case[j]
  return case

t = int(input())
case = []

for _ in range(t):
  case.append(int(input()))

for data in bubble_sort(case):
  print(data)

# 파이썬 정렬 라이브러리를 사용하면 
t = int(input())
result = [] 
for _ in range(t):
  result.append(int(input()))

result.sort()
for data in result:
  print(data)

from typing import list