# merge sort 10번 연습하기 
from typing import List

def merge1(nums: List[int]) -> List[int]:
  length = len(nums)
  if length == 1:
    return nums
  
  mid = length // 2

  left = nums[:mid]
  right = nums[mid:]

  sorted_left = merge1(left)
  sorted_right = merge1(right)

  result = []
  left_idx = 0
  right_idx = 0

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      result.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      result.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_right[right_idx] >= sorted_left[left_idx]:
      result.append(sorted_left[left_idx])
      left_idx += 1

    else:
      result.append(sorted_right[right_idx])
      right_idx += 1
  return result

print("merge1 = ", merge1(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))


def merge2(nums: List[int]) -> List[int]:
  length = len(nums)
  if length == 1:
    return nums
  
  mid = length // 2
  left = nums[:mid]
  right = nums[mid:]  

  sorted_left = merge2(left) 
  sorted_right = merge2(right)

  result = []
  left_idx = 0
  right_idx = 0

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      result.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      result.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_right[right_idx] >= sorted_left[left_idx]:
      result.append(sorted_left[left_idx])
      left_idx += 1

    else:
      result.append(sorted_right[right_idx])
      right_idx += 1
  
  return result

print("merge2 = ", merge2(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))


def merge3(nums: List[int]) -> List[int]:
  length = len(nums)
  if length == 1:
    return nums

  mid = length // 2
  left = nums[:mid]
  right = nums[mid:]

  sorted_left = merge3(left)
  sorted_right = merge3(right)

  result = []
  left_idx = 0
  right_idx = 0

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      result.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      result.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_left[left_idx] >= sorted_right[right_idx]:
      result.append(sorted_right[right_idx])
      right_idx += 1

    else:
      result.append(sorted_left[left_idx])
      left_idx += 1

  return result

print("merge3 = ", merge3(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def merge4(nums: List[int]) -> List[int]:
  if len(nums) == 1:
    return nums
  
  mid = len(nums) // 2
  left = nums[:mid]
  right = nums[mid:]

  sorted_left = merge4(left)
  sorted_right = merge4(right)

  result = []
  left_idx = 0
  right_idx = 0

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      result.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      result.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_left[left_idx] >= sorted_right[right_idx]:
      result.append(sorted_right[right_idx])
      right_idx += 1

    else:
      result.append(sorted_left[left_idx])
      left_idx += 1

  return result

print("merge4 = ", merge4(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8])) 

def merge5(nums:List[int]) -> List[int]:
  if len(nums) == 1:
    return nums
  
  mid = len(nums) // 2
  left = nums[:mid]
  right = nums[mid:]  

  sorted_left = merge5(left)
  sorted_right = merge5(right)

  result = []
  left_idx = 0
  right_idx = 0

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      result.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      result.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_left[left_idx] >= sorted_right[right_idx]:
      result.append(sorted_right[right_idx])
      right_idx += 1

    else:
      result.append(sorted_left[left_idx])
      left_idx += 1

  return result

print("merge5 = ", merge5(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def merge6(nums: List[int]) -> List[int]:
  if len(nums) == 1:
    return nums
  
  mid = len(nums) // 2
  left = nums[:mid]
  right = nums[mid:]  

  sorted_left = merge6(left)
  sorted_right = merge6(right)

  result = []
  left_idx = 0
  right_idx = 0

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      result.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      result.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_left[left_idx] >= sorted_right[right_idx]:
      result.append(sorted_right[right_idx])
      right_idx += 1

    else:
      result.append(sorted_left[left_idx])
      left_idx += 1

  return result

print("merge6 = ", merge6(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def merge7(nums: List[int]) -> List[int]:
  if len(nums) == 1:
    return nums
  
  mid = len(nums) // 2
  left = nums[:mid]
  right = nums[mid:] 

  sorted_left = merge7(left)
  sorted_right = merge7(right)

  result = []
  left_idx = 0
  right_idx = 0

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      result.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      result.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_left[left_idx] >= sorted_right[right_idx]:
      result.append(sorted_right[right_idx])
      right_idx += 1

    else:
      result.append(sorted_left[left_idx])
      left_idx += 1

  return result

print("merge7 = ", merge7(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

def merge8(nums: List[int]) -> List[int]:
  if len(nums) == 1:
    return nums
  
  mid = len(nums) // 2
  left = nums[:mid]
  right = nums[mid:] 

  sorted_left = merge8(left)
  sorted_right = merge8(right)

  result = []
  left_idx = 0
  right_idx = 0

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      result.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      result.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_left[left_idx] >= sorted_right[right_idx]:
      result.append(sorted_right[right_idx])
      right_idx += 1

    else:
      result.append(sorted_left[left_idx])
      left_idx += 1

  return result

print("merge8 = ", merge8(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))


def merge9(nums: List[int]) -> List[int]:

  if len(nums) == 1:
    return nums

  mid = len(nums) // 2
  left = nums[:mid]
  right = nums[mid:]

  sorted_left = merge9(left)
  sorted_right = merge9(right)

  result = []
  left_idx = 0
  right_idx = 0

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      result.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      result.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_left[left_idx] >= sorted_right[right_idx]:
      result.append(sorted_right[right_idx])
      right_idx += 1

    else:
      result.append(sorted_left[left_idx])
      left_idx += 1
  
  return result

print("merge9 = ", merge9(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))


def merge10(nums:List[List]) -> List[int]:
  if len(nums) == 1:
    return nums

  mid = len(nums) // 2
  left = nums[:mid]
  right = nums[mid:]

  sorted_left = merge10(left) 
  sorted_right = merge10(right)

  result = []
  left_idx = 0
  right_idx = 0

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      result.append(sorted_right[right_idx])
      right_idx += 1
      continue
      

    if right_idx == len(sorted_right):
      result.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_left[left_idx] >= sorted_right[right_idx]:
      result.append(sorted_right[right_idx])
      right_idx += 1

    else:
      result.append(sorted_left[left_idx])
      left_idx += 1    
  return result

print("merge10 = ", merge10(nums = [1,9,4,3,5,5,6,6,7,3,2,2,8]))

