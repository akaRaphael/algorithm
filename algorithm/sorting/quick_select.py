# Quick Select

# 1) Quick Select 개념 
#   - 정렬되지 않은 배열의 n번째 크거나 작은 수를 찾을 때 사용하는 알고리즘
#   - pivot을 선정하여 pivot보다 작은 수는 좌측에, pivot보다 큰 수는 우측에 정렬한다.
#   - n번째 큰 수를 찾는 경우, pivot의 우측에 위치한 요소를 대상으로 알고리즘을 다시 적용한다. 
#   - n번째 작은 수를 찾는 경우, pivot의 좌측에 위치한 요소를 대상으로 알고리즘을 다시 적용한다.
#   - 이 과정을 재귀적으로 반복하여 n번째 수를 찾는다. 

from typing import List
import random

# k번째 큰 수를 반환하는 경우 
def quick_select(case: List[int], k: int) -> int:
  length = len(case)
  if length == 1:
    return case[0]

  pivot_idx = random.randrange(length)
  last_idx = length - 1

  # 최초에 pivot을 지정한 뒤에 배열의 가장 우측의 요소와 swap한다. 
  case[pivot_idx], case[last_idx] = case[last_idx], case[pivot_idx]

  # pivot보다 작은 수인지 판단할 포인터
  left_idx = 0 

  # pivot보다 큰 수인지 판단할 포인터 
  # -2를 하는 이유는 len() 메소드는 총 요소의 개수를 반환하기 때문이고, 맨 우측의 pivot을 제외하기 위함 
  right_idx = length - 2
  
  pivot = case[-1]  

  while left_idx <= right_idx: # 두 개의 포인터가 교차하면 종료 

    if case[left_idx] <= pivot: # 좌측 포인터가 pivot보다 작은 경우, 우측으로 이동 
      left_idx += 1
      continue

    if pivot < case[right_idx]: # 우측 포인터가 pivot보다 큰 경우, 좌측으로 이동
      right_idx -= 1
      continue

    if pivot < case[left_idx] and pivot >= case[right_idx]: # 두 포인터가 더이상 이동하지 못하는 경우 
      case[left_idx], case[right_idx] = case[right_idx], case[left_idx] # 두 포인터가 가리키는 값을 swap
      continue
  
  # quick select를 한바퀴 돌으면, left_idx가 pivot의 우측에 정렬되는 수 중에 가장 왼쪽의 수를 가리킨다. 
  case[left_idx], case[last_idx] = case[last_idx], case[left_idx]
  if left_idx == length - k: # 좌측 포인터가 가리키는 index가 찾고 있는 index인 경우 
    return case[left_idx]

  elif left_idx < length - k: # pivot의 우측에 있는 수 중에 찾고 있는 수가 있는 경우
    return quick_select(case = case[left_idx + 1:], k = k) # 우측의 요소를 대상으로 quick select를 다시 적용
    # left_idx + 1을 하는 이유는, 현재 left_idx가 가리키는 수는 찾는 수가 아니므로 고려 대상에서 제외하기 때문

  elif length - k < left_idx: # pivot의 좌측에 있는 수 중에 찾고 있는 수가 있는 경우
    return quick_select(case = case[:left_idx], k = k - (length - left_idx)) # 좌측의 요소를 대상으로 quick select를 다시 적용
    # k - (length - left_idx)를 하는 이유는, 좌측의 수 만을 대상으로 배열을 형성하는 경우, 요소 개수의 변화로 타겟 index가 달라지기 때문이다. 

print(quick_select(case = [4,2,1,3,5], k = 2))