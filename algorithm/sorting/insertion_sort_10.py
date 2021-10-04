# insertion sort 10번 연습하기 

from typing import List

def insertion_sort1(nums: List[int]) -> List[int]:
  for idx in range(1, len(nums)):
    flag = idx - 1
    current = nums[idx]

    while flag >= 0 and current < nums[flag]:
      nums[flag + 1] = nums[flag]
      flag -= 1
    nums[flag + 1] = current
  return nums

print("insertion1 = ", insertion_sort1(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def insertion_sort2(nums: List[int]) -> List[int]:
  for idx in range(1, len(nums)):
    flag = idx - 1
    current = nums[idx]

    while flag >= 0 and current < nums[flag]:
      nums[flag + 1] = nums[flag]
      flag -= 1
    nums[flag + 1] = current
  return nums

print("insertion2 = ", insertion_sort2(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def insertion_sort3(nums: List[int]) -> List[int]:
  for idx in range(1, len(nums)):
    flag = idx - 1
    current = nums[idx]

    while flag >= 0 and current < nums[flag]:
      nums[flag + 1] = nums[flag]
      flag -= 1
    nums[flag + 1] = current
  return nums

print("insertion3 = ", insertion_sort3(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))  

def insertion_sort4(nums: List[int]) -> List[int]:
  for idx in range(1, len(nums)):
    flag = idx - 1
    current = nums[idx]

    while flag >= 0 and current < nums[flag]:
      nums[flag + 1] = nums[flag]
      flag -= 1
    nums[flag + 1] = current
  return nums

print("insertion4 = ", insertion_sort4(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))


def insertion_sort5(nums: List[int]) -> List[int]:
  for idx in range(1, len(nums)):
    flag = idx - 1
    current = nums[idx]

    while flag >= 0 and current < nums[flag]:
      nums[flag + 1] = nums[flag]
      flag -= 1
    nums[flag + 1] = current
  return nums

print("insertion5 = ", insertion_sort5(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))


def insertion_sort6(nums: List[int]) -> List[int]:
  for idx in range(1, len(nums)):
    flag = idx - 1
    current = nums[idx]

    while flag >= 0 and current < nums[flag]:
      nums[flag + 1] = nums[flag]
      flag -= 1
    nums[flag + 1] = current
  return nums

print("insertion6 = ", insertion_sort6(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def insertion_sort7(nums: List[int]) -> List[int]:
  for idx in range(1, len(nums)):
    flag = idx - 1
    current = nums[idx]

    while flag >= 0 and current < nums[flag]:
      nums[flag + 1] = nums[flag]
      flag -= 1
    nums[flag + 1] = current
  return nums

print("insertion7 = ", insertion_sort7(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def insertion_sort8(nums: List[int]) -> List[int]:
  for idx in range(1, len(nums)):
    flag = idx - 1
    current = nums[idx]

    while flag >= 0 and current < nums[flag]:
      nums[flag + 1] = nums[flag]
      flag -= 1
    nums[flag + 1] = current
  return nums

print("insertion8 = ", insertion_sort8(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def insertion_sort9(nums: List[int]) -> List[int]:
  for idx in range(1, len(nums)):
    flag = idx - 1
    current = nums[idx]

    while flag >= 0 and current < nums[flag]:
      nums[flag + 1] = nums[flag]
      flag -= 1
    nums[flag + 1] = current
  return nums
print("insertion9 = ", insertion_sort9(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def insertion_sort10(nums: List[int]) -> List[int]:
  for idx in range(1, len(nums)):
    flag = idx - 1
    current = nums[idx]

    while flag >= 0 and current < nums[flag]:
      nums[flag + 1] = nums[flag]
      flag -= 1
    nums[flag + 1] = current
  return nums
print("insertion10 = ", insertion_sort10(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))