# quick select 10번 연습하기 

from typing import List
import random

def quick_select1(nums: List[int], k:int) -> int:
  length = len(nums)
  if length == 1:
    return nums[0]
  
  pivot_idx = random.randrange(length)
  last_idx = length -1 

  nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]
  left_idx = 0
  right_idx = length - 2
  pivot = nums[-1]

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
  if left_idx == length - k:
    return nums[left_idx]
    
  elif left_idx < length - k:
    return quick_select1(nums = nums[left_idx + 1:], k = k)
    
  elif left_idx > length - k:
    return quick_select1(nums = nums[:left_idx], k = k - (length - left_idx))

print(quick_select1(nums = [9,8,7,6,5,4,3,2,1], k = 2))


def quick_select2(nums: List[int], k: int) -> int:
  length = len(nums)
  if length == 1:
    return nums[0]

  pivot_idx = random.randrange(length)
  last_idx = length - 1

  nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]

  left_idx = 0
  right_idx = length -2 
  pivot = nums[-1]

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
  if left_idx == length - k:
    return nums[left_idx]
  elif left_idx < length - k:
    return quick_select2(nums = nums[left_idx + 1:], k = k)
  elif left_idx > length - k:
    return quick_select2(nums = nums[:left_idx], k = k - (length - left_idx))

print(quick_select2(nums = [9,9,5,4,4,8,7,6,5,4,3,2,1], k = 4))

def qs3(nums: List[int], k: int) -> int:
  length = len(nums)
  if length == 1:
    return nums[0]

  pivot_idx = random.randrange(length)
  last_idx = length - 1

  nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]

  left_idx = 0
  right_idx = length - 2
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
  if left_idx == length - k:
    return nums[left_idx]
  
  elif left_idx <= length - k:
    return qs3(nums = nums[left_idx + 1:], k = k)
  
  elif left_idx > length - k:
    return qs3(nums = nums[:left_idx], k = k - (length - left_idx))
  
print(qs3(nums = [9,9,5,4,4,8,7,6,5,4,3,2,1], k = 4))


def qs4(nums: List[int], k: int) -> int:
  length = len(nums)
  if length == 1:
    return nums[0]

  pivot_idx = random.randrange(length)
  last_idx = length - 1

  nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]

  left_idx = 0
  right_idx = length - 2
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
  if left_idx == length - k:
    return nums[left_idx]
  
  elif left_idx < length - k:
    return qs4(nums = nums[left_idx + 1:], k = k)
  
  elif left_idx > length - k:
    return qs4(nums = nums[:left_idx], k = k - (length - left_idx))

print(qs4(nums = [9,9,5,4,4,8,7,6,5,4,3,2,1], k = 4))


def qs5(nums: List[int], k: int) -> int:
  length = len(nums)
  if length == 1:
    return nums[0]
  
  pivot_idx = random.randrange(length)
  last_idx = length - 1

  nums[last_idx], nums[pivot_idx] = nums[pivot_idx], nums[last_idx]

  left_idx = 0
  right_idx = length -2
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
  if left_idx == length - k:
    return nums[left_idx]

  elif left_idx < length - k:
    return qs5(nums = nums[left_idx + 1:], k = k)
  
  elif left_idx > length - k:
    return qs5(nums = nums[:left_idx], k = k - (length - left_idx))
  
print(qs5(nums = [9,9,5,4,4,8,7,6,5,4,3,2,1], k = 4))

def qs6(nums: List[int], k: int) -> int:
  length = len(nums)
  if length == 1:
    return nums[0]

  pivot_idx = random.randrange(length)
  last_idx = length - 1

  nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]

  left_idx = 0
  right_idx = length - 2
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
  if left_idx == length - k:
    return nums[left_idx]
  
  elif left_idx < length - k:
    return qs6(nums = nums[left_idx + 1:], k = k)
  
  elif left_idx > length - k:
    return qs6(nums = nums[:left_idx], k = k - (length - left_idx))

print(qs6(nums = [9,9,5,4,4,8,7,6,5,4,3,2,1], k = 7))

def qs7(nums: List[int], k: int) -> int:
  length = len(nums)
  if length == 1:
    return nums[0]
  
  last_idx = length - 1
  pivot_idx = random.randrange(length)

  nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]

  left_idx = 0
  right_idx = length - 2
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

  if left_idx == length - k:
    return nums[left_idx]

  elif left_idx < length - k:
    return qs7(nums = nums[left_idx + 1:], k = k)
  
  elif left_idx > length - k:
    return qs7(nums = nums[:left_idx], k = k - (length - left_idx))
  
print(qs7(nums = [9,9,5,4,4,8,7,6,5,4,3,2,1], k = 7))

def qs8(nums: List[int], k: int) -> int:
  length = len(nums)  
  if length == 1:
    return nums[0] 

  pivot_idx = random.randrange(length)
  last_idx = length - 1

  nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]

  left_idx = 0
  right_idx = length - 2
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
  if left_idx == length - k:
    return nums[left_idx]
  
  elif left_idx < length - k:
    return qs8(nums = nums[left_idx + 1:], k = k)
  
  elif left_idx > length - k:
    return qs8(nums = nums[:left_idx], k = k - (length - left_idx))

print(qs8(nums = [9,9,5,4,4,8,7,6,5,4,3,2,1], k = 7))
  
def qs9(nums: List[int], k: int) -> int:
  length = len(nums)
  if length == 1:
    return nums[0]
  
  pivot_idx = random.randrange(length)
  last_idx = length - 1

  nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]

  left_idx = 0
  right_idx = length - 2
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

  if left_idx == length - k:
    return nums[left_idx]
  
  elif left_idx < length - k:
    return qs9(nums = nums[left_idx + 1:], k = k)

  elif left_idx > length - k:
    return qs9(nums = nums[:left_idx], k = k - (length - left_idx))

print(qs9(nums = [9,9,5,4,4,8,7,6,5,4,3,2,1], k = 7))


def qs10(nums:List[int], k:int) -> int:
  length = len(nums)  
  if length == 1:
    return nums[0]

  pivot_idx = random.randrange(length)
  last_idx = length - 1
  nums[last_idx], nums[pivot_idx] = nums[pivot_idx], nums[last_idx]

  left_idx = 0
  right_idx = length -2
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

  if left_idx == length - k:
    return nums[left_idx]

  elif left_idx < length - k:
    return qs10(nums = nums[left_idx + 1:], k = k)
  
  elif left_idx > length - k:
    return qs10(nums = nums[:left_idx], k = k - (length - left_idx))

print(qs10(nums = [9,9,5,4,4,8,7,6,5,4,3,2,1], k = 7))
  

