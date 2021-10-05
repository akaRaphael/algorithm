# heap sort 10번 연습하기 
from typing import List
import heapq

def hs1(nums: List[int]) -> List[int]:
  nums = [-1 * n for n in nums]
  heapq.heapify(nums)

  sorted = [0] * len(nums)

  for i in range(len(nums) - 1, -1, -1):
    largest = -1 * heapq.heappop(nums)
    sorted[i] = largest
  
  return sorted

print(hs1(nums = [3, 5, 7, 9, 4, 2]))


def hs2(nums: List[int]) -> List[int]:
  nums = [-1 * data for data in nums]
  heapq.heapify(nums)

  sorted = [0] * len(nums)

  for i in range(len(nums) - 1, -1, -1):
    largest = -1 * heapq.heappop(nums)
    sorted[i] = largest
  return sorted

print(hs2(nums = [3, 5, 9, 7, 4, 2]))

def hs3(nums: List[int]) -> List[int]:
  nums = [ -1 * num for num in nums]
  heapq.heapify(nums)

  max_heap = [0] * len(nums)

  for i in range(len(nums) - 1, -1, -1):
    largest = -1 * heapq.heappop(nums)
    max_heap[i] = largest
  return max_heap

print(hs3(nums = [3, 5, 9, 7, 4, 2]))


def hs4(nums: List[int]) -> List[int]:
  nums = [-1 * data for data in nums]
  heapq.heapify(nums)

  max_heap = [0] * len(nums)

  for i in range(len(nums) - 1, -1, -1):
    largest = -1 * heapq.heappop(nums)
    max_heap[i] = largest
  return max_heap

print(hs4(nums = [3, 5, 9, 7, 4, 2]))

def hs5(nums:List[int]) -> List[int]:
  nums = [-1 * num for num in nums]
  heapq.heapify(nums)

  max_heap = [0] * len(nums)

  for i in range(len(nums) - 1, -1, -1):
    largest = -1 * heapq.heappop(nums)
    max_heap[i] = largest
  return max_heap

print(hs5(nums = [3, 5, 9, 7, 4, 2]))

def hs6(nums: List[int]) -> List[int]:
  nums = [-1 * data for data in nums]
  heapq.heapify(nums)

  maxheap = [0] * len(nums)

  for i in range(len(nums) - 1, -1, -1):
    largest = heapq.heappop(nums)
    maxheap[i] = -1 * largest
  return maxheap

print(hs6(nums = [3, 5, 9, 7, 4, 2]))

def hs7(nums: List[int]) -> List[int]:
  nums = [-1 * num for num in nums]
  heapq.heapify(nums)
  maxheap = [0] * len(nums)

  for i in range(len(nums) - 1, -1, -1):
    largest = heapq.heappop(nums)
    maxheap[i] = -1 * largest
  return maxheap

print(hs7(nums = [3, 5, 9, 7, 4, 2]))

def hs8(nums: List[int]) -> List[int]:
  nums = [-1 * num for num in nums]
  heapq.heapify(nums)
  maxheap = [0] * len(nums)

  for i in range(len(nums) - 1, -1, -1):
    largest = heapq.heappop(nums)
    maxheap[i] = -1 * largest
  return maxheap

print(hs8(nums = [3, 5, 9, 7, 4, 2]))

def hs9(nums: List[int]) -> List[int]:
  nums = [-1 * data for data in nums]
  heapq.heapify(nums)
  maxheap = [0] * len(nums)

  for i in range(len(nums) - 1, -1, -1):
    largest = heapq.heappop(nums)
    maxheap[i] = largest * -1
  return maxheap
print(hs9(nums = [3, 5, 9, 7, 4, 2]))

def hs10(nums: List[int]) -> List[int]:
  nums = [-1 * data for data in nums]
  heapq.heapify(nums)
  maxheap = [0] * len(nums)

  for i in range(len(nums) - 1, -1, -1):
    largest = heapq.heappop(nums)
    maxheap[i] = largest * -1
  return maxheap

print(hs10(nums = [3, 5, 9, 7, 4, 2]))