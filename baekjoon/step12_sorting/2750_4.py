# 백준 단계별 풀이 12단계 - 수 정렬하기 
# https://www.acmicpc.net/problem/2750

# 선택정렬을 사용해서 풀어보자. 
from typing import List
from sys import stdin
input = stdin.readline

def selection_sort(case: List[int]) -> List[int]:
  for idx in range(len(case)):
    min_num = case[idx]
    min_idx = idx
    for i in range(idx, len(case)):
      if case[i] < min_num:
        min_num = case[i]
        min_idx = i
    case[idx], case[min_idx] = case[min_idx], case[idx]
  return case

t = int(input())
case = []
for _ in range(t):
  case.append(int(input()))

print("\n".join(map(str, selection_sort(case))))