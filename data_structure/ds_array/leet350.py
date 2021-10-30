# 350. Intersection of Two Arrays II

from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
  i = 0
  result = []
  while i < len(nums1):
    if nums1[i] in nums2:
      result.append(nums1[i])
      nums2.pop(nums2.index(nums1[i]))
    i += 1
  return result
    
print(intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))


