# 88. Merge Sorted Array

from typing import List

class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    length = len(nums1) - 1
    for i in range(len(nums2)):
      nums1[length-i] = nums2[i]
    nums1.sort()

class Solution2:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    length = len(nums1) - m
    for i in range(length):
      nums1[m + i] = nums2[i]
    nums1.sort()
