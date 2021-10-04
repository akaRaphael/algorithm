# selection sort 10번 연습하기 
from typing import List

def selection1(nums: List[int]) -> List[int]:
  for idx in range(len(nums)):
    min_num = nums[idx]
    min_idx = idx

    for i in range(idx, len(nums)):
      if min_num > nums[i]:
        min_num = nums[i]
        min_idx = i
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
  return nums

print("selection1 = ", selection1(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def selection2(nums: List[int]) -> List[int]:
  for idx in range(len(nums)):
    min_num = nums[idx]
    min_idx = idx

    for i in range(idx, len(nums)):
      if min_num > nums[i]:
        min_num = nums[i]
        min_idx = i
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
  return nums

print("selection2 = ", selection2(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def selection3(nums: List[int]) -> List[int]:
  for idx in range(len(nums)):
    min_idx = idx
    min_num = nums[idx]

    for i in range(idx, len(nums)):
      if min_num > nums[i]:
        min_num = nums[i]
        min_idx = i
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
  return nums

print("selection3 = ", selection3(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def selection4(nums: List[int]) -> List[int]:
  for idx in range(len(nums)):
    min_num = nums[idx]
    min_idx = idx

    for i in range(idx, len(nums)):
      if min_num > nums[i]:
        min_num = nums[i]
        min_idx = i
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
  return nums

print("selection4 = ", selection4(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def selection5(nums: List[int]) -> List[int]:
  for idx in range(len(nums)):
    min_idx = idx
    min_num = nums[idx]

    for i in range(idx, len(nums)):
      if min_num > nums[i]:
        min_num = nums[i]
        min_idx = i
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
  return nums

print("selection5 = ", selection5(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def selection6(nums: List[int]) -> List[int]:
  for idx in range(len(nums)):
    min_num = nums[idx]
    min_idx = idx

    for i in range(idx, len(nums)):
      if min_num > nums[i]:
        min_num = nums[i]
        min_idx = i
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
  return nums

print("selection6 = ", selection6(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def selection7(nums: List[int]) -> List[int]:
  for idx in range(len(nums)):
    min_num = nums[idx]
    min_idx = idx

    for i in range(idx, len(nums)):
      if min_num > nums[i]:
        min_num = nums[i]
        min_idx = i
    nums[min_idx], nums[idx] = nums[idx], nums[min_idx]
  return nums

print("selection7 = ", selection7(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def selection8(nums: List[int]) -> List[int]:
  for idx in range(len(nums)):
    min_num = nums[idx]
    min_idx = idx

    for i in range(idx, len(nums)):
      if min_num > nums[i]:
        min_num = nums[i]
        min_idx = i
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
  return nums

print("selection8 = ", selection8(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def selection9(nums: List[int]) -> List[int]:
  for idx in range(len(nums)):
    min_num = nums[idx]
    min_idx = idx

    for i in range(idx, len(nums)):
      if min_num > nums[i]:
        min_num = nums[i]
        min_idx = i
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
  return nums

print("selection9 = ", selection9(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def selection10(nums: List[int]) -> List[int]:
  for idx in range(len(nums)):
    min_idx = idx 
    min_num = nums[idx]

    for i in range(idx, len(nums)):
      if min_num > nums[i]:
        min_num = nums[i]
        min_idx = i
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
  return nums

print("selection10 = ", selection10(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))