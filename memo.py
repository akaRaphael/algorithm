# 21년 9월 15일 총 복습 

from typing import List

def bubble_sort(case:List[int]) -> List[int]:
  for idx in range(len(case) - 1):
    for i in range(len(case) - idx - 1):
      if case[i] > case[i + 1]:
        case[i], case[i + 1] = case[i + 1], case[i]
  return case

def insertion_sort(case: List[int]) -> List[int]:
  for idx in range(1, len(case)):
    flag = idx - 1
    current = case[idx]
    while flag >= 0 and current < case[flag]:
      case[flag + 1] = case[flag]
      flag -= 1
    case[flag + 1] = current
  return case

def selection_sort(case: List[int]) -> List[int]:
  for idx in range(len(case)):
    min_num = case[idx]
    min_idx = idx
    for i in range(idx, len(case)):
      if min_num > case[i]:
        min_num = case[i]
        min_idx = i
    case[idx], case[min_idx] = case[min_idx], case[idx]
  return case

def merge_sort(case:List[int]) -> List[int]:
  length = len(case)
  if length == 1:
    return case
  
  mid = length // 2
  left_case = case[:mid]
  right_case = case[mid:]

  sorted_left = merge_sort(left_case)
  sorted_right = merge_sort(right_case)

  sorted_case = []
  left_idx = 0
  right_idx = 0

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      sorted_case.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      sorted_case.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_right[right_idx] >= sorted_left[left_idx]:
      sorted_case.append(sorted_left[left_idx])
      left_idx += 1

    else:
      sorted_case.append(sorted_right[right_idx])
      right_idx += 1

  return sorted_case


import random
def quick_select(case: List[int], k:int) -> int:
  length = len(case)
  if length == 1:
    return case[0]
  
  pivot_idx = random.randrange(length)
  last_idx = length - 1

  case[pivot_idx], case[last_idx] = case[last_idx], case[pivot_idx]
  left_idx = 0
  right_idx = length - 2
  pivot = case[-1]

  while left_idx <= right_idx:
    if case[left_idx] <= pivot:
      left_idx += 1
      continue

    if case[right_idx] > pivot:
      right_idx -= 1
      continue

    if case[right_idx] < pivot and case[left_idx] > pivot:
      case[right_idx], case[left_idx] = case[left_idx], case[right_idx]
      continue

  case[left_idx], case[last_idx] = case[last_idx], case[left_idx]

  if left_idx == length - k:
    return case[left_idx]
  
  elif left_idx <= length - k:
    return quick_select(case = case[left_idx + 1:], k = k)

  elif left_idx >= length - k:
    return quick_select(case = case[:left_idx], k = k - (length - left_idx))


def quick_sort(case:List[int], begin_idx:int, last_idx:int) -> List[int]:
  length = last_idx - begin_idx + 1
  if length <= 1:
    return case
  
  pivot_idx = random.randrange(begin_idx, last_idx + 1)
  case[pivot_idx], case[last_idx] = case[last_idx], case[pivot_idx]
  left_idx = 0
  right_idx = last_idx - 1
  pivot = case[last_idx]

  while left_idx <= right_idx:
    if case[left_idx] <= pivot:
      left_idx += 1
      continue

    if case[right_idx] > pivot:
      right_idx -= 1
      continue

    if pivot < case[left_idx] and pivot >= case[right_idx]:
      case[left_idx], case[right_idx] = case[right_idx], case[left_idx]
      continue
  case[left_idx], case[last_idx] = case[last_idx], case[left_idx]
  quick_sort(case = case, begin_idx = left_idx + 1, last_idx = last_idx)
  quick_sort(case = case, begin_idx = begin_idx, last_idx = left_idx - 1)

  return case


import heapq
def heap_sort(case: List[int]) -> List[int]:
  case = [-1 * n for n in case]
  heapq.heapify(case)

  sorted_case = [0] * len(case)

  for i in range(len(case) - 1, -1, -1):
    sorted_case[i] =  -1 * heapq.heappop(case)
  
  return sorted_case

print("bubble_sort =", bubble_sort(case = [9,10,11,13,14,15,16,1,5,6,7,8,3,2]))
print("insertion_sort =", insertion_sort(case = [9,10,11,13,14,15,16,1,5,6,7,8,3,2]))
print("selection_sort =", selection_sort(case = [9,10,11,13,14,15,16,1,5,6,7,8,3,2]))
print("merge_sort =", merge_sort(case = [9,10,11,13,14,15,16,1,5,6,7,8,3,2]))
print("quick_select =", quick_select(case = [9,10,11,13,14,15,16,1,5,6,7,8,3,2], k = 2)) # k번째 큰수 찾기 인데, 작은 수 찾기는 어떻게 할까? 

case = [9,10,11,13,14,15,16,1,5,6,7,8,3,2]
quick_sort(case = case, begin_idx = 0, last_idx = len(case) - 1)
print("quick_sort =", case)
print("heap_sort =", heap_sort(case = [9,10,11,13,14,15,16,1,5,6,7,8,3,2]))