# bubble sort
# 1) bubble sort 개념
# bubble 이란? - 배열의 두개의 요소를 하나의 묶어 놓은 것 
# bubble swap 이란? 
#    - 어떤 기준을 기반으로 bubble로 묶인 두개의 요소를 비교한다.
#    - 비교하여 두 요소의 위치를 바꿔준다. [A, B] ==> [B, A]

# 2) bubble sort의 안정성(stability)
#   - bubble sort는 stable한 정렬 알고리즘이다. 

# 3) bubble sort의 시간복잡도(time complexity)
#   - bubble sort는 n개의 요소를 n번 탐색한다.
#   - 그러므로 O(n^2)의 시간복잡도를 갖는다. 

# 4) bubble sort 구현    
from typing import List

def bubble(nums: List[int]) -> List[int]:
  for idx in range(0, len(nums) - 1):
    for i in range(0, len(nums) - idx - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i] #swap
  return nums

print(bubble(nums=[9,3,5,7,1])) # [1, 3, 5, 7, 9] 를 출력 

# 4) bubble sort의 안정성 확인 
def bubble2(num_str):
  for idx in range(0, len(num_str) - 1):
    for i in range(0, len(num_str) - idx - 1):
      if num_str[i][0] > num_str[i + 1][0]:
        num_str[i], num_str[i + 1] = num_str[i + 1], num_str[i] #swap
  return num_str

num_str = [(7, 'A'), (5, 'A'), (5, 'B'), (7, 'B'), (3, 'C')]
print(bubble2(num_str))

# 내가 구현한 bubble sort
case = [6, 2, 5, 1, 7, 4, 3]
for idx in range(len(case) - 1):
  for i in range(len(case) - idx - 1):
    if case[i] > case[i + 1]:
      case[i], case[i + 1] = case[i + 1], case[i]
print(case)



