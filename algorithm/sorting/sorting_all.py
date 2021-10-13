# sorting 알고리즘 총정리

from typing import List

def bubble_sort(nums: List[int]) -> List[int]:
  for idx in range(0, len(nums) - 1):
    for i in range(0, len(nums) - idx - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
  return nums

print("bubble_sort = ", bubble_sort(nums = [9,8,7,7,6,5,4,3,2,1]))

#####################################################################

def insertion_sort(nums: List[int]) -> List[int]:
  for idx in range(1, len(nums)):
    flag = idx - 1
    current = nums[idx]

    while flag >= 0 and current < nums[flag]:
      nums[flag + 1] = nums[flag]
      flag -= 1
    nums[flag + 1] = current
  return nums
 
print("insertion_sort = ", insertion_sort(nums = [5,5,6,7,4,4,3,2,1]))

#####################################################################

def selection_sort(nums: List[int]) -> List[int]:
  for idx in range(len(nums)):
    min_num = nums[idx]
    min_idx = idx
    for i in range(idx, len(nums)):
      if min_num > nums[i]:
        min_num = nums[i]
        min_idx = i

    nums[min_idx], nums[idx] = nums[idx], nums[min_idx]
  return nums

print("selection_sort =", selection_sort(nums = [9,8,7,7,6,5,4,3,2,1]))

#####################################################################

def merge_sort(nums: List[int]) -> List[int]:
  length = len(nums)
  if length == 1:
    return nums
  
  mid = length // 2
  left = nums[:mid] 
  right = nums[mid:]

  sorted_left = merge_sort(nums = left)
  sorted_right = merge_sort(nums = right)

  left_idx = 0
  right_idx = 0
  sorted = []

  while left_idx < len(sorted_left) or right_idx < len(sorted_right):
    if left_idx == len(sorted_left):
      sorted.append(sorted_right[right_idx])
      right_idx += 1
      continue

    if right_idx == len(sorted_right):
      sorted.append(sorted_left[left_idx])
      left_idx += 1
      continue

    if sorted_left[left_idx] >= sorted_right[right_idx]:
      sorted.append(sorted_right[right_idx])
      right_idx += 1

    else:
      sorted.append(sorted_left[left_idx])
      left_idx += 1

  return sorted

print("merge_sort =", merge_sort(nums = [9,8,7,7,6,5,4,3,2,1]))

#####################################################################

import random
def quick_select(nums: List[int], k: int) -> int:
  length = len(nums)
  if length == 1:
    return nums[0]
  
  mid = length // 2
  left = nums[:mid]
  right = nums[mid:]  

  pivot_idx = random.randrange(length)
  last_idx = length - 1

  nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]
  pivot = nums[last_idx]
  left_idx = 0
  right_idx = length - 2

  while left_idx <= right_idx:
    if nums[left_idx] < pivot:
      left_idx += 1
      continue

    if nums[right_idx] >= pivot:
      right_idx -= 1
      continue

    if nums[left_idx] > pivot and nums[right_idx] <= pivot:
      nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
  
  nums[left_idx], nums[last_idx] = nums[last_idx], nums[left_idx]

  if left_idx == length - k:
    return nums[left_idx]

  elif left_idx < length - k:
    return quick_select(nums = nums[left_idx + 1:], k = k)
  
  elif left_idx > length - k:
    return quick_select(nums = nums[:left_idx], k = k - (length - left_idx))

print("quick_select =", quick_select(nums = [9,8,7,7,6,5,4,3,2,1], k = 5))

#####################################################################

def quick_sort(nums: List[int], begin_idx: int, last_idx: int) -> List[int]:
  length = last_idx - begin_idx + 1
  if length <= 1:
    return nums
  
  mid = length // 2
  left = nums[:mid]
  right = nums[mid:]  
  pivot_idx = random.randrange(begin_idx, last_idx + 1)

  nums[last_idx], nums[pivot_idx] = nums[pivot_idx], nums[last_idx]
  pivot = nums[last_idx]

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

  quick_sort(nums = nums, begin_idx = left_idx + 1, last_idx = last_idx)
  quick_sort(nums = nums, begin_idx = 0, last_idx = left_idx - 1)

  return nums

nums = [9,8,7,7,6,5,4,3,2,1]
quick_sort(nums = nums, begin_idx = 0, last_idx = len(nums) - 1)
print("quick_sort = ", nums)

#####################################################################
import heapq

def heap_sort(nums: List[int]) -> List[int]:
  nums = [data * -1 for data in nums]
  heapq.heapify(nums)
  max_heap = [0] * len(nums)

  for i in range(len(nums) - 1, -1, -1):
    largest = heapq.heappop(nums) * -1
    max_heap[i] = largest
  return max_heap

print("heap_sort =", heap_sort(nums = [9,8,7,7,6,5,4,3,2,1]))

#####################################################################

def counting_sort(nums: List[int]) -> List[int]:
  max_num = max(nums)
  min_num = min(nums)
  count_length = max_num - min_num  + 1
  count_array = [0] * count_length

  for num in nums:
    count_idx = num - min_num
    count_array[count_idx] += 1

  acc_count = 0
  acc_array = []
  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)

  end_locs = [data - 1 for data in acc_array]
  sorted = [0] * len(nums)

  for num in reversed(nums):
    count_idx = num - min_num
    end_loc = end_locs[count_idx]
    sorted[end_loc] = num
    end_locs[count_idx] -= 1

  return sorted

print("counting_sort =", counting_sort(nums = [5,5,5,6,7,8,8,9,3,2,2,1]))

#####################################################################

import math
def counting_radix(nums: List[int], digit: int) -> List[int]:
  count_array = [0] * 10
  for num in nums:
    count_idx = num // pow(10, digit) % 10
    count_array[count_idx] += 1

  acc_count = 0
  acc_array = []
  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)

  end_locs = [d - 1 for d in acc_array]
  sorted = [0] * len(nums)

  for num in reversed(nums):
    count_idx = num // pow(10, digit) % 10
    end_loc = end_locs[count_idx]
    sorted[end_loc] = num
    end_locs[count_idx] -= 1

  return sorted

def radix_sort(nums: List[int]) -> List[int]:
  largest = max(nums)
  digits = int(math.log10(largest)) + 1
  sorted = nums

  for digit in range(digits):
    sorted = counting_radix(nums = sorted, digit = digit)

  return sorted

print("radix_sort =", radix_sort(nums = [583,555,599,634,752,8,311,222,2,1]))