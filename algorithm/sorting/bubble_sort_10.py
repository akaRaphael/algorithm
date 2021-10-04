# bubble sort 10번 연습하기 

from typing import List

def bubble_sort1(nums: List[int]) -> List[int]:
  for idx in range(len(nums) - 1):
    for i in range(len(nums) - idx - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
  return nums

print("bubble_sort1 = ", bubble_sort1(nums = [9,8,7,6,5,5,4,3,3,2,1]))

def bubble_sort2(nums: List[int]) -> List[int]:
  for idx in range(len(nums) - 1):
    for i in range(len(nums) - idx - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
  return nums

print("bubble_sort2 = ", bubble_sort2(nums = [9,8,7,6,5,5,4,3,3,2,1]))

def bubble_sort3(nums: List[int]) -> List[int]:
  for idx in range(0, len(nums) - 1):
    for i in range(0, len(nums) - idx - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
  return nums

print("bubble_sort3 = ", bubble_sort3(nums = [9,8,7,6,5,5,4,3,3,2,1]))


def bubble_sort4(nums: List[int]) -> List[int]:
  for idx in range(0, len(nums) - 1):
    for i in range(0, len(nums) - idx - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
  return nums

print("bubble_sort4 = ", bubble_sort4(nums = [9,8,7,6,5,5,4,3,3,2,1]))


def bubble_sort5(nums: List[int]) -> List[int]:
  for idx in range(0, len(nums) - 1):
    for i in range(0, len(nums) - idx - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
  return nums

print("bubble_sort5 = ", bubble_sort5(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def bubble_sort6(nums: List[int]) -> List[int]:
  for idx in range(len(nums) - 1):
    for i in range(len(nums) - idx - 1):
      if nums[i] > nums[i + 1]:
        nums[i] , nums[i + 1] = nums[i + 1], nums[i]  
  return nums

print("bubble_sort6 = ", bubble_sort6(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def bubble_sort7(nums: List[int]) -> List[int]:
  for idx in range(len(nums) - 1):
    for i in range(len(nums) - idx - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
  return nums

print("bubble_sort7 = ", bubble_sort7(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def bubble_sort8(nums: List[int]) -> List[int]:
  for idx in range(len(nums) - 1):
    for i in range(len(nums) - idx - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
  return nums

print("bubble_sort8 = ", bubble_sort8(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def bubble_sort9(nums: List[int]) -> List[int]:
  for idx in range(len(nums) - 1):
    for i in range(len(nums) - idx - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
  return nums

print("bubble_sort9 = ", bubble_sort9(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def bubble_sort10(nums: List[int]) -> List[int]:
  for idx in range(len(nums) - 1):
    for i in range(len(nums) - idx - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
  return nums

print("bubble_sort10 = ", bubble_sort10(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))
