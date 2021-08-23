# 백준 단계별 풀이 12단계 - 수 정렬하기 
# https://www.acmicpc.net/problem/2750

# 삽입정렬을 사용해서 풀어보자. 
from typing import List
from sys import setprofile, stdin
input = stdin.readline

def insertion_sort(case: List[int]) -> List[int]:
  for idx in range(1, len(case)):
    current = case[idx]
    flag = idx - 1
    while flag >= 0 and current < case[flag]:
      case[flag + 1] = case[flag]
      flag = flag - 1
    case[flag + 1] = current
  return case

t = int(input())
case = []

for _ in range(t):
  case.append(int(input()))

print("\n".join(map(str, insertion_sort(case))))