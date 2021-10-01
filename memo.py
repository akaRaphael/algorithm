# 21년 10월 1일 정렬알고리즘 총 복습

# bubble sort
from typing import List

def bubble_sort(nums:List[int]) -> List[int]:
  for idx in range(0, len(nums)):
    for i in range(0, len(nums) - idx - 1):
      if nums[i + 1] < nums[i]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
  return nums

print(bubble_sort(nums = [9,8,7,6,5,4,3,2,1]))

# insertion sort
def insertion_sort(nums:List[int]) -> List[int]:
  for idx in range(1, len(nums)):
    flag = idx - 1
    current = nums[idx]

    while flag >= 0 and current < nums[flag]:
      nums[flag + 1] = nums[flag]
      flag = flag - 1
    nums[flag + 1] = current
  return nums

print(insertion_sort(nums = [9,8,7,6,5,4,3,2,1]))

# selection sort
def selection_sort(nums:List[int]) -> List[int]:
  for idx in range(0, len(nums)):
    min_num = nums[idx]
    min_idx = idx

    for i in range(idx, len(nums)):
      if min_num > nums[i]:
        min_num = nums[i]
        min_idx = i
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
  return nums

print(selection_sort(nums = [9,8,7,6,5,4,3,2,1]))

# Merge Sort
def merge_sort(nums:List[int]) -> List[int]:
  length = len(nums)
  if length == 1:
    return nums
  
  mid = length // 2

  left_nums = nums[:mid]
  right_nums = nums[mid:]

  sorted_left = merge_sort(nums = left_nums)
  sorted_right = merge_sort(nums = right_nums)

  left_idx = 0
  right_idx = 0
  result = []

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      result.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      result.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_right[right_idx] <= sorted_left[left_idx]:
      result.append(sorted_right[right_idx])
      right_idx += 1

    else:
      result.append(sorted_left[left_idx])
      left_idx += 1
  return result

print(merge_sort(nums = [9,8,7,6,5,4,3,2,1]))

# quick select
import random

def quick_select(nums:List[int], k:int) -> int:
  length = len(nums)
  if length == 1:
    return nums[0]
  
  pivot_idx = random.randrange(len(nums))
  last_idx = length - 1

  nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]

  left_idx = 0
  right_idx = length - 2

  pivot = nums[-1]

  while left_idx <= right_idx:
    if nums[left_idx] <= pivot:
      left_idx += 1
      continue

    if nums[right_idx] >= pivot:
      right_idx -= 1
      continue

    if nums[left_idx] > pivot and nums[right_idx] <= pivot:
      nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
      continue

  nums[left_idx], nums[last_idx] = nums[last_idx], nums[left_idx]

  if left_idx == length - k:
    return nums[left_idx]

  if left_idx < length - k:
    return quick_select(nums[left_idx + 1:], k)

  if left_idx > length - k:
    return quick_select(nums[:left_idx], k - length - left_idx)

print(quick_select(nums = [9,8,7,6,5,4,3,2,1], k = 3))

# quick_sort
def quick_sort(nums:List[int], begin_idx:int, end_idx:int) -> List[int]:

  length = end_idx - begin_idx + 1
  if length <= 1:
    return nums
  
  pivot_idx = random.randrange(begin_idx, end_idx + 1)
  nums[pivot_idx], nums[end_idx] = nums[end_idx], nums[pivot_idx]
  left_idx = 0
  right_idx = end_idx - 1
  pivot = nums[end_idx]

  while left_idx <= right_idx:
    if nums[left_idx] <= pivot:
      left_idx += 1
      continue

    if nums[right_idx] > pivot:
      right_idx -= 1
      continue

    if nums[left_idx] > pivot and nums[right_idx] <= pivot:
      nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
      continue

  nums[left_idx], nums[end_idx] = nums[end_idx], nums[left_idx]

  quick_sort(nums = nums, begin_idx = left_idx + 1, end_idx = end_idx)
  quick_sort(nums = nums, begin_idx = begin_idx, end_idx = left_idx - 1)

  return nums

nums = [9,8,7,6,5,4,3,2,1]
quick_sort(nums = nums, begin_idx = 0, end_idx = len(nums) - 1)
print(nums)





