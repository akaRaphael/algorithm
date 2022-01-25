# Leet Code - DS 익히기 14일 챌린지 
# https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
      length = len(nums1) - m
      for i in range(length):
        nums1[m + i] = nums2[i]
         
      nums1.sort()
      print(nums1)

foo = Solution()
foo.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
        