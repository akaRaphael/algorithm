from typing import List

def countingSort(nums:List[int])->List[int]:  
  length = len(nums)
  min_num = min(nums)  #offset
  max_num = max(nums)

  range = max_num - min_num + 1
  counts = [0]*range

  for num in nums:
    count_idx = num - min_num
    counts[count_idx] += 1

  acc_counts = []
  acc_count = 0
  for count in counts:
    acc_count += count
    acc_counts.append(acc_count)

  end_locs = [ c-1 for c in acc_counts]

  sorted = [0] * length
  for num in reversed(nums):
    count_idx = num - min_num
    end_loc = end_locs[count_idx]
    sorted[end_loc] = num
    end_locs[count_idx] -= 1

  return sorted

print(countingSort(nums=[3,4,0,1,2]))
print(countingSort(nums=[3,0,5,1,0,5]))