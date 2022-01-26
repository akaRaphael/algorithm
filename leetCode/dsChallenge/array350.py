# # Leet Code - DS 익히기 14일 챌린지 
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

from typing import List

class Solution:
  def intersect(self, nums1:List[int], nums2:List[int]) -> List[int]:
    answer = []
    for num in nums1:
      if num in nums2:
        answer.append(num)
        nums2.pop(nums2.index(num))
        
    return answer
      
    

foo = Solution()
print(foo.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))