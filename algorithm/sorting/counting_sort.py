from typing import List

def countingSort(nums:List[int])->List[int]:  
  length = len(nums)
  min_num = min(nums) # 가장 작은 수 
  max_num = max(nums) # 가장 큰 수 

  range = max_num - min_num + 1 # count array를 만들기 위한 크기 설정 
  count_array = [0] * range # count array 생성 

  for num in nums: # count array의 요소를 채우는 과정 
    count_idx = num - min_num # min_num이 0이 아닌 경우, index 0번이 비어있게 되기 때문에 이를 방지하기 위함.
    count_array[count_idx] += 1

  acc_counts = [] # acc(누적) array 생성 
  acc_count = 0 # acc array의 요소가 될 값 
  for count in count_array: # acc array의 요소를 채우는 과정 
    acc_count += count
    acc_counts.append(acc_count)

  end_locs = [ c-1 for c in acc_counts] # acc array - 1 배열을 만드는 과정 

  sorted = [0] * length # 최종적으로 정렬될 배열 생성 
  for num in reversed(nums): # 맨 뒤의 요소부터 정렬을 시작하는데, 이를 리버스로 구현 
    count_idx = num - min_num
    end_loc = end_locs[count_idx]
    sorted[end_loc] = num
    end_locs[count_idx] -= 1

  return sorted

print(countingSort(nums=[3,4,0,1,2]))
print(countingSort(nums=[3,0,5,1,0,5]))