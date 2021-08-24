# selection sort(선택정렬)

# 1) selection sort 개념
# - 가장 왼쪽의 수(index == 0)를 기준으로 최소값을 찾아 swap하여 정렬하는 알고리즘
# - 최소값과 swap하면 기준 index가 한칸씩 옆으로 이동한다. 

# 2) selection sort의 안정성(stability)
# - selection sort는 unstable한 정렬 알고리즘이다. 
# - 아래의 예제를 참고하자. 

# 3) selection sort의 시간복잡도(time complexity)
# - 버블정렬, 삽입정렬과 동일한 O(n^2)의 시간복잡도를 갖는다. 

# 4) selection sort 내가 구현해보기
# - selection sort의 동작과정을 기반으로 직접 구현해 보았다.  
from typing import List

def selection_sort(case: List[int]) -> List[int]:
  for idx in range(1, len(case)):
    flag = idx - 1
    temp = 0
    min_idx = 0 
    while idx < len(case):
      if case[flag] > case[idx]:
        diff = case[flag] - case[idx]
        if diff > temp:
          temp = diff
          min_idx = idx
      idx += 1
      if idx == len(case) and min_idx != 0:
        case[flag], case[min_idx] = case[min_idx], case[flag]
  return case

print(selection_sort(case = [9, 3, 7, 1, 5]))

# 5) selection sort 코드
def selection_sort2(case: List[int]) -> List[int]:
  for idx in range(0, len(case)):
    min_num = case[idx]
    min_idx = idx
    for i in range(idx, len(case)):
      if case[i] < min_num:
        min_num = case[i]
        min_idx = i
    case[idx], case[min_idx] = case[min_idx], case[idx] #swap
  return case

print(selection_sort2(case = [5, 4, 3, 2, 1]))