# Merge Sort
# 1) Merge Sort의 개념 
#   - 하나의 배열을 반씩 쪼개어 요소의 총 개수만큼 독립된 배열을 만든다.
#   - 반씩 쪼개진 배열을 Left, Right로 구분한다. 
#   - Left에 있는 배열끼리, Right에 있는 배열끼리의 요소를 비교하여 병합한다.
#   - 비교 후 병합하는 과정을 반복하여 최종적으로 하나의 정렬된 배열을 만든다. 
#   - 이 과정을 재귀적으로 구현해낸다.  

# 2) Merge Sort의 시간복잡도(Time Complexity)
#   - 배열을 반씩 쪼개는 과정 => O(log n)
#   - 각각의 독립된 배열 요소간의 비교를 통한 병합과정 => O(n)
#   - 최종적으로 O(log n) * O(n) => O(n log n)의 시간복잡도를 갖는다. 

# 3) Merge Sort의 안정성(Stability)
#   - Merge Sort는 Stable한 정렬 알고리즘이다. 

# 4) Merge Sort 구현 
from typing import List

def merge_sort(case: List[int]) -> List[int]:

  # 반으로 쪼개기
  length = len(case)
  if length == 1:
    return case
  
  # 중간지점 index 찾기 
  mid = length // 2

  # 반으로 나누어 Left, Right로 분류하기 
  left_case = case[:mid]
  right_case = case[mid:]

  # 재귀적으로 length가 1일 때까지 반으로 나누고 정렬하기 
  # left_case부터 정렬을 시작한다.
  # left_case의 정렬이 완료된 후 right_case의 정렬이 시작된다.  
  sorted_left = merge_sort(case = left_case)
  sorted_right = merge_sort(case = right_case)

  # 비교 및 병합과정 
  sorted_case = []
  left_idx = 0
  right_idx = 0

  # 배열의 길이보다 작은 경우 = left_idx 또는 right_idx가 가리킬 다음 요소가 있는 경우
  while left_idx < len(sorted_left) or right_idx < len(sorted_right):

    # 만약 left_idx가 더이상 가리킬 다음 요소가 없는 경우 
    # right_idx가 현재 가리키는 수를 결과 배열에 병합한다. 
    if left_idx == len(sorted_left):
      sorted_case.append(sorted_right[right_idx])
      right_idx += 1
      continue

    # 만약 right_idx가 더이상 가리킬 요소가 없는 경우,
    # left_idx가 현재 가리키는 수를 결과 배열에 병합한다. 
    if right_idx == len(sorted_right):
      sorted_case.append(sorted_left[left_idx])
      left_idx += 1
      continue

    # 만약 right_idx가 가리키는 요소가 left_idx가 가리키는 요소보다 작은 경우,
    # right_idx가 가리키는 요소를 결과 배열에 병합한다. 
    if sorted_right[right_idx] <= sorted_left[left_idx]:
      sorted_case.append(sorted_right[right_idx])
      right_idx += 1

    # 만약 left_idx가 가리키는 요소가 right_idx가 가리키는 요소보다 작은 경우
    # left_idx가 가리키는 요소를 결과 배열에 병합한다. 
    else:
      sorted_case.append(sorted_left[left_idx])
      left_idx += 1

  return sorted_case

print(merge_sort(case = [8,7,6,5,4,3,2,1]))
