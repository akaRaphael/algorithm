# # Radix Sort 10번 연습하기 

from typing import List
import math

def countingSortByDigit(nums: List[int], digit: int) -> List[int]:
  counts = [0] * 10 
  for num in nums:
    count_idx = num // pow(10, digit) % 10
    counts[count_idx] += 1

  acc_array = []
  acc_count = 0
  for count in counts:
    acc_count += count
    acc_array.append(acc_count)
  end_locs = [data - 1 for data in acc_array]

  sorted = [0] * len(nums)
  for num in reversed(nums):
    count_idx = num // pow(10, digit) % 10
    end_loc = end_locs[count_idx]
    sorted[end_loc] = num
    end_locs[count_idx] -= 1
  
  return sorted

def radixSort(nums: List[int]) -> List[int]:
  largest_num = max(nums)
  digits = int(math.log10(largest_num)) + 1
  sorted = nums
  for digit in range(digits):
    sorted = countingSortByDigit(nums = sorted, digit = digit)
  return sorted

print(radixSort(nums=[391,582,50,924,8,192]))

def cs2(nums: List[int], digit: int) -> List[int]:
  count_array = [0] * 10
  for num in nums:
    count_idx = num // pow(10, digit) % 10
    count_array[count_idx] += 1
  
  acc_array = []
  acc_count = 0
  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)
  
  end_locs = [data - 1 for data in acc_array]
  sorted = [0] * len(nums)
  for num in reversed(nums):
    count_idx = num // pow(10, digit) % 10
    end_loc = end_locs[count_idx]
    sorted[end_loc] = num
    end_locs[count_idx] -= 1
  
  return sorted

def rs2(nums: List[int]) -> List[int]:
  largest = max(nums)
  digits = int(math.log10(largest)) + 1
  sorted = nums
  for digit in range(digits):
    sorted = cs2(nums = sorted, digit = digit)
  return sorted

print(rs2(nums=[391,582,50,924,8,192]))

def cs3(nums: List[int], digit: int) -> List[int]:
  count_array = [0] * 10
  for num in nums:
    count_idx = num // pow(10, digit) % 10
    count_array[count_idx] += 1

  acc_array = []
  acc_count = 0
  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)

  end_locs = [data - 1 for data in acc_array]
  sorted = [0] * len(nums)

  for num in reversed(nums):
    count_idx = num // pow(10, digit) % 10
    end_loc = end_locs[count_idx]
    sorted[end_loc] = num
    end_locs[count_idx] -= 1

  return sorted

def rs3(nums: List[int]) -> List[int]:
  largest = max(nums)
  digits = int(math.log10(largest)) + 1
  sorted = nums
  for digit in range(digits):
    sorted = cs3(nums = sorted, digit = digit)
  return sorted

print(rs3(nums=[192,582,352,452,52,2]))

def cs4(nums: List[int], digit: int) -> List[int]:
  count_array = [0] * 10 
  for num in nums:
    count_idx = num // pow(10, digit) % 10
    count_array[count_idx] += 1

  acc_array = []
  acc_count = 0
  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)
  
  end_locs = [data - 1 for data in acc_array]
  sorted = [0] * len(nums)

  for num in reversed(nums):
    count_idx = num // pow(10, digit) % 10 
    end_loc = end_locs[count_idx]
    sorted[end_loc] = num
    end_locs[count_idx] -= 1
  return sorted

def rs4(nums: List[int]) -> List[int]:
  largest = max(nums)
  digits = int(math.log10(largest)) + 1
  sorted = nums
  for digit in range(digits):
    sorted = cs4(nums = sorted, digit = digit)
  return sorted

print(rs4(nums=[192,582,352,452,52,2]))