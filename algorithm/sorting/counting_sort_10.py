# counting sort 10번 연습하기
from typing import List

def cs1(nums: List[int]) -> List[int]:
  length = len(nums)
  min_num = min(nums)
  max_num = max(nums)

  # count array 생성
  count_length = max_num - min_num + 1
  count_array = [0] * count_length

  for num in nums:
    count_idx = num - min_num
    count_array[count_idx] += 1

  # accumulated array 생성
  acc_array = []
  acc_count = 0

  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)

  # acc_array -1 생성
  end_locs = [ data - 1 for data in acc_array]

  # 정렬
  result = [0] * length 
  for num in reversed(nums):
    count_idx = num - min_num
    end_loc = end_locs[count_idx]
    result[end_loc] = num
    end_locs[count_idx] -= 1
  
  return result

print(cs1(nums=[3,5,1,1,2]))

def cs2(nums: List[int]) -> List[int]:
  length = len(nums)
  min_num = min(nums)
  max_num = max(nums)

  # count_array
  count_length = max_num - min_num + 1
  count_array = [0] * count_length

  for num in nums:
    count_idx = num - min_num
    count_array[count_idx] += 1
  
  # acc_array
  acc_array = []
  acc_count = 0

  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)

  # end_locs
  end_locs = [data - 1 for data in acc_array]

  # 정렬
  result = [0] * length
  for num in reversed(nums):
    count_idx = num - min_num
    end_loc = end_locs[count_idx]
    result[end_loc] = num
    end_locs[count_idx] -= 1
  
  return result

print(cs2(nums=[3,5,1,1,2]))

def cs3(nums: List[int]) -> List[int]:
  length = len(nums)
  min_num = min(nums)
  max_num = max(nums)

  count_length = max_num - min_num + 1
  count_array = [0] * count_length 

  for num in nums:
    count_idx = num - min_num
    count_array[count_idx] += 1

  acc_array = []
  acc_count = 0

  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)

  end_locs = [ data - 1 for data in acc_array]
  result = [0] * length

  for num in reversed(nums):
    count_idx = num - min_num
    end_loc = end_locs[count_idx]
    result[end_loc] = num
    end_locs[count_idx] -= 1

  return result

print(cs3(nums=[3,5,1,1,2,4,7,6,6,3,0]))


def cs4(nums: List[int]) -> List[int]:
  length = len(nums)
  min_num = min(nums)
  max_num = max(nums)

  #count_array
  count_length = max_num - min_num + 1
  count_array = [0] * count_length

  for num in nums:
    count_idx = num - min_num
    count_array[count_idx] += 1

  #acc_array
  acc_array = []
  acc_count = 0

  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)

  # acc_array - 1
  acc_array = [data - 1 for data in acc_array]
  result = [0] * length 

  for num in reversed(nums):
    count_idx = num - min_num
    acc_idx = acc_array[count_idx]
    result[acc_idx] = num
    acc_array[count_idx] -= 1
  
  return result

print(cs4(nums=[3,5,1,1,2,4,7,6,6,3,0]))

def cs5(nums: List[int]) -> List[int]:
  length = len(nums)
  max_num = max(nums)
  min_num = min(nums)

  # count_array
  count_length = max_num - min_num + 1
  count_array = [0] * count_length 

  for num in nums:
    count_idx = num - min_num 
    count_array[count_idx] += 1

  # acc_array
  acc_array = []
  acc_count = 0

  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)

  end_locs = [ data - 1 for data in acc_array]
  result = [0] * length

  for num in reversed(nums):
    count_idx = num - min_num
    end_loc = end_locs[count_idx]
    result[end_loc] = num
    end_locs[count_idx] -= 1

  return result

print(cs5(nums=[3,5,1,1,2,4,7,6,6,3,0]))

def cs6(nums: List[int]) -> List[int]:
  length = len(nums)
  min_num = min(nums)
  max_num = max(nums)

  # count_array
  count_length = max_num - min_num + 1
  count_array = [0] * count_length 

  for num in nums:
    count_idx = num - min_num
    count_array[count_idx] += 1

  # acc_array
  acc_array = []
  acc_count = 0

  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)

  # acc_array - 1
  end_locs = [data - 1 for data in acc_array]

  # 정렬
  result = [0] * length
  for num in reversed(nums):
    count_idx = num - min_num
    end_loc = end_locs[count_idx]
    result[end_loc] = num
    end_locs[count_idx] -= 1

  return result

print(cs6(nums=[3,5,2,4,7,6,6,3,0]))

def cs7(nums: List[int]) -> List[int]:
  length = len(nums)
  min_num = min(nums)
  max_num = max(nums)

  # count_array
  count_length = max_num - min_num + 1
  count_array = [0] * count_length

  for num in nums:
    count_idx = num - min_num
    count_array[count_idx] += 1

  # acc_array
  acc_count = 0
  acc_array = []

  for count in count_array:
     acc_count += count
     acc_array.append(acc_count)
    
  # acc_array - 1
  end_locs = [data - 1 for data in acc_array]

  # sorting
  result = [0] * length
  for num in reversed(nums):
    count_idx = num - min_num
    end_loc = end_locs[count_idx]
    result[end_loc] = num
    end_locs[count_idx] -= 1
  
  return result

print(cs7(nums=[3,5,2,4,7,6,6,3,0]))

def cs8(nums: List[int]) -> List[int]:
  length = len(nums)
  max_num = max(nums)
  min_num = min(nums)

  # count_array
  count_length = max_num - min_num + 1
  count_array = [0] * count_length

  for num in nums:
    count_idx = num - min_num
    count_array[count_idx] += 1

  # acc_array
  acc_count = 0
  acc_array = []

  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)

  # end_locs
  end_locs = [data - 1 for data in acc_array]

  # 정렬
  result = [0] * length
  for num in nums:
    count_idx = num - min_num
    end_loc = end_locs[count_idx]
    result[end_loc] = num
    end_locs[count_idx] -= 1

  return result

print(cs8(nums=[3,5,2,4,7,6,6,3,0]))

def cs9(nums: List[int]) -> List[int]:
  length = len(nums)
  max_num = max(nums)
  min_num = min(nums)

  # count array
  count_length = max_num - min_num + 1
  count_array = [0] * count_length

  for num in nums:
    count_idx = num - min_num
    count_array[count_idx] += 1

  # acc_array
  acc_count = 0
  acc_array = []

  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)

  # end_locs
  end_locs = [data - 1 for data in acc_array]

  # sorting
  result = [0] * length

  for num in nums:
    count_idx = num - min_num
    end_loc = end_locs[count_idx]
    result[end_loc] = num
    end_locs[count_idx] -= 1

  return result

print(cs9(nums=[0,0,0,1,1,1,2,4,7,6,6,3,5]))

def cs10(nums: List[int]) -> List[int]:
  length = len(nums)
  max_num = max(nums)
  min_num = min(nums)

  # count array
  count_length = max_num - min_num + 1
  count_array = [0] * count_length

  for num in nums:
    count_idx = num - min_num
    count_array[count_idx] += 1

  # acc array
  acc_count = 0
  acc_array = []

  for count in count_array:
    acc_count += count
    acc_array.append(acc_count)
  
  end_locs = [data - 1 for data in acc_array]
  result  = [0] * length

  for num in nums:
    count_idx = num - min_num
    end_loc = end_locs[count_idx]
    result[end_loc] = num
    end_locs[count_idx] -= 1

  return result

print(cs10(nums=[0,0,0,1,1,1,2,4,7,6,6,3,5]))






   
