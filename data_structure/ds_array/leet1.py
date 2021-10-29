# 1. Two Sum
from typing import List

# def twoSum(nums: List[int], target: int) -> List[int]:
  # for i in range(len(nums)):
  #   find_num = target - nums[i]
  #   try: 
  #     if nums.index(find_num) != i:
  #       return i, nums.index(find_num)
  #   except:
  #     continue

def twoSum(nums: List[int], target: int) -> List[int]:  
  extra={}
  for i in range(len(nums)):
    diff=target-nums[i]
    if diff in extra:
      return [i,extra[diff]]
    extra[nums[i]]=i
    print(extra)

print(twoSum(nums = [3,3,1], target = 6))
print(twoSum(nums = [-1,-2,-3,-4,-5], target = -8))
print(twoSum(nums = [3,2,95,4,-3], target = 92))
