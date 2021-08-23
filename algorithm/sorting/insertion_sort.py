# insertion sort

# 1) insertion sort 개념
# - 가장 왼쪽의 수(index == 0)를 기준으로 다음 요소와 기준 값의 크기를 비교한다.
# - 비교를 통해 기준값의 왼쪽 또는 오른쪽에 삽입하여 배열을 정렬하는 알고리즘

# 2) insertion sort의 안정성(stability)
# - insertion sort는 stable한 정렬 알고리즘이다. 

# 3) insertion sort의 시간복잡도(time complexity)
# - 버블정렬과 동일한 O(n^2)의 시간복잡도를 갖는다. 

# 4) insertion sort 구현 
from typing import List

def insertion_sort(case: List[int]) -> List[int]:
  for idx in range(1, len(case)):
    current = case[idx] # 기준 값과 비교될 요소
    flag = idx - 1 # 기준 값의 index 
    
    while flag >= 0 and current < case[flag]: 
      # 1) 기준값의 index(= flag)가 0보다 크거나 같아야 한다. 
      #    올바른 정렬이 진행된다면, 기준값은 0으로부터 멀어지기 때문이다. 

      # 2) current가 기준값 보다 작아야 한다.
      #    그렇지 않다면, 기준값을 이동시킬 이유가 없다. 
      #    이미 기준값 보다 뒤에 위치하기 때문
    
      case[flag + 1] = case[flag] 
      # 기준값의 현재 위치에서 한칸 뒤로 이동시킨다.

      flag = flag - 1
      # current를 기준값 보다 한칸 앞으로 옮기기 전에 
      # 기준값의 앞에 다른 요소가 있을 수 있다. 
      # 기준값 앞의 다른 요소와 current의 크기를 비교한다. 
      # 이 과정을 반복해서 current가 삽입될 위치를 정한다. 

    case[flag + 1] = current 
    # while문에서 current가 삽입될 위치를 찾는다. 
    # 해당 위치에 current를 삽입한다. 

  return case

print(insertion_sort(case = [9, 3, 5, 7, 1]))