# quick sort 5번 연습하기 

from typing import List
import random

def qs1(nums: List[int], begin_idx: int, last_idx: int) -> List[int]:
  length = last_idx - begin_idx + 1
  if length <= 1:
    return nums

  pivot_idx = random.randrange(begin_idx, last_idx + 1)
  nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]

  left_idx = 0
  right_idx = last_idx - 1
  pivot = nums[last_idx]

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
  
  nums[left_idx], nums[last_idx] = nums[last_idx], nums[left_idx]
  
  qs1(nums = nums, begin_idx = left_idx + 1, last_idx = last_idx)
  qs1(nums = nums, begin_idx = begin_idx, last_idx = left_idx - 1)

  return nums

nums = [5, 7, 9, 3, 1, 5, 5, 2, 4]
qs1(nums = nums, begin_idx = 0, last_idx = len(nums) - 1)
print(nums)

def qs2(nums: List[int], begin_idx: int, last_idx: int) -> List[int]:
  length = last_idx - begin_idx + 1
  if length <= 1:
    return nums
  
  pivot_idx = random.randrange(begin_idx, last_idx + 1)
  nums[pivot_idx], nums[last_idx] = nums[pivot_idx], nums[last_idx]

  left_idx = 0
  right_idx = last_idx - 1
  pivot = nums[last_idx]

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

  nums[left_idx], nums[last_idx] = nums[last_idx], nums[left_idx]

  qs2(nums = nums, begin_idx = left_idx + 1, last_idx = last_idx)
  qs2(nums = nums, begin_idx = begin_idx, last_idx = left_idx - 1)

nums = [5, 7, 9, 3, 1, 5, 5, 2, 4]
qs2(nums = nums, begin_idx = 0, last_idx = len(nums) - 1)
print(nums)


def qs3(nums: List[int], begin_idx: int, last_idx: int) -> List[int]:
  length = last_idx - begin_idx + 1
  if length <= 1:
    return nums
  
  pivot_idx = random.randrange(begin_idx, last_idx + 1)
  nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]

  left_idx = 0
  right_idx = last_idx - 1
  pivot = nums[last_idx]

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

  nums[left_idx], nums[last_idx] = nums[last_idx], nums[left_idx]

  qs3(nums = nums, begin_idx = left_idx + 1, last_idx = last_idx)
  qs3(nums = nums, begin_idx = begin_idx, last_idx = left_idx - 1)

nums = [5, 7, 9, 3, 1, 5, 5, 2, 4]
qs3(nums = nums, begin_idx = 0, last_idx = len(nums) - 1)
print(nums)

def qs4(nums: List[int], begin_idx: int, last_idx: int) -> List[int]:
  length = last_idx - begin_idx + 1
  if length <= 1:
    return nums
  
  pivot_idx = random.randrange(begin_idx, last_idx + 1)
  nums[pivot_idx], nums[last_idx] = nums[last_idx] = nums[pivot_idx]

  left_idx = 0
  right_idx = last_idx - 1
  pivot = nums[last_idx]

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

  nums[left_idx], nums[last_idx] = nums[last_idx], nums[left_idx]

  qs4(nums = nums, begin_idx = left_idx + 1, last_idx = last_idx)
  qs4(nums = nums, begin_idx = begin_idx, last_idx = left_idx - 1)

nums = [5, 7, 9, 3, 1, 5, 5, 2, 4]
qs2(nums = nums, begin_idx = 0, last_idx = len(nums) - 1)
print(nums)

def qs5(nums: List[int], begin_idx: int, last_idx: int) -> List[int]:
  length = last_idx - begin_idx + 1
  if length <= 1:
    return nums
  
  pivot_idx = random.randrange(begin_idx, last_idx + 1)
  nums[last_idx], nums[pivot_idx] = nums[pivot_idx], nums[last_idx]

  left_idx = 0
  right_idx = last_idx - 1
  pivot = nums[last_idx]

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

  nums[left_idx], nums[last_idx] = nums[last_idx], nums[left_idx]

  qs5(nums = nums, begin_idx = left_idx + 1, last_idx = last_idx)
  qs5(nums= nums, begin_idx = begin_idx, last_idx = left_idx - 1) 

nums = [5, 7, 9, 3, 1, 5, 5, 2, 4]
qs5(nums = nums, begin_idx = 0, last_idx = len(nums) - 1)
print(nums)
