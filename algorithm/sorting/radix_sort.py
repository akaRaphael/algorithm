# Radix Sort

from typing import List
import math

def countingSortByDigit(nums:List[int],digit:int)->List[int]:  
  counts = [0]*10
  for num in nums:
    count_idx = num//pow(10,digit)%10
    counts[count_idx] += 1

  acc_counts = []
  acc_count = 0
  for count in counts:
    acc_count += count
    acc_counts.append(acc_count)
  end_locs = [ c-1 for c in acc_counts]

  sorted = [0] * len(nums)
  for num in reversed(nums):
    count_idx = num//pow(10,digit)%10
    end_loc = end_locs[count_idx]
    sorted[end_loc] = num
    end_locs[count_idx] -= 1

  return sorted


def radixSort(nums:List[int])->List[int]:
  largest_num = max(nums)
  digits = int(math.log10(largest_num))+1
  sorted = nums
  for digit in range(digits):
    sorted = countingSortByDigit(nums=sorted,digit=digit)
  return sorted

print(radixSort(nums=[391,582,50,924,8,192]))