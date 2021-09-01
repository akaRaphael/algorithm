# 백준 단계별 풀이 12단계 - 수 정렬하기 2
# https://www.acmicpc.net/problem/2751

# merge sort(병합정렬)를 사용해서 풀어보자

from sys import stdin
from typing import List
input = stdin.readline

def merge_sort(case: List[int]) -> List[int]:
  length = len(case)
  if length == 1:
    return case
  
  mid = length // 2
  left_case = case[:mid] 
  right_case = case[mid:]

  result = []
  left_idx = 0
  right_idx = 0
  sorted_left = merge_sort(left_case)
  sorted_right = merge_sort(right_case)

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      result.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      result.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_left[left_idx] <= sorted_right[right_idx]:
      result.append(sorted_left[left_idx])
      left_idx += 1

    else:
      result.append(sorted_right[right_idx])
      right_idx += 1
  
  return result


n = int(input())
case = []

for _ in range(n):
  case.append(int(input()))

case = merge_sort(case = case)
print("\n".join(map(str, case)))