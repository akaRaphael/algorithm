# 1) Heap 이란?
# - 최대값/최소값 검색을 목적으로 하는 완전이진트리를 말한다.

# 2) Heap의 구조 
# - Heap은 Max-heap과 min-heap으로 구분된다. 
# - Max Heap은 root 노드가 최대값을 유지하는 완전이진트리 
#    - 부모노드가 자식노드보다 크거나 같다 
# - Min Heap은 root 노드가 최소값을 유지하는 완전이진트리 
#    - 부모노드가 자식노드보다 작거나 같다

# 3) Heap과 이진탐색트리의 공통점 
# - Heap과 이진탐색트리는 모두 완전이진트리를 기반한 자료구조다.

# 4) Heap과 이진탐색트리의 차이점 
# - Heap과 이진탐색트리는 형제노드간의 규칙에서 차이를 갖는다.
# - 이진탐색트리는 좌측노드(자식) < 부모노드 < 우측노드(자식)의 규칙을 갖는다.
# - Heap은 형제노드간의 규칙이 없고 부모/자식노드간의 규칙은 존재한다.

# 5) Heap의 기본동작 

#  a. 삽입과정 
#   - 완전이진트리를 기반하므로, 노드가 삽입될 때 최하단 좌측 노드부터 채워진다. 
#   - 삽입 후 Min/Max-heap의 여부에 따라 swap하며 정렬이 진행된다. 

#  b. 추출/삭제과정
#   - Min/Max-heap 모두 최상단노드(root)가 추출/삭제된다.   
#   - root 노드가 추출되고 나면, 가장 마지막에 삽입된 노드가 root에 올라간다.
#   - 이후 Min/Max-heap의 여부에 따라 swap하며 정렬이 진행된다. 

# 6) Heap의 규칙성 
# - Heap은 완전이진트리로 단말노드 외 부모노드는 반드시 2개의 자식노드를 소유한다.
# - 그러므로 자식노드의 위치를 이용해 부모노드의 위치를 구하는 공식이 존재한다. 
#     => 부모노드 = 자식노드 번호 // 2 
# - 반대로 부모노드의 위치를 이용해 자식노드의 위치를 알 수 있다.
#     => 우측 자식노드  = 부모노드 번호 * 2 + 1
#     => 좌측 자식노드 = 부모노드 번호 * 2 + 1

# 7) 리스트를 이용한 Max Heap 구현 
class Heap():
  def __init__(self, data):
    self.heap_array = list()
    self.heap_array.append(None)  
    self.heap_array.append(data)
    
  def checkSorting(self, insert_index): 
    # 삽입된 데이터의 위치에 따라 정렬이 필요한지 검사 
    if insert_index < 2: # heap에 아무 데이터도 없는 경우 
      return False
    else:
      parent_index = insert_index // 2
      if self.heap_array[insert_index] > self.heap_array[parent_index]:
        return True
      else:
        return False

  def insert(self, data):
    if len(self.heap_array) == 0: # heap이 비어있는 경우 
      self.heap_array.append(None)
      self.heap_array.append(data)
      return True
    else: # heap에 데이터가 존재하는 경우 
      self.heap_array.append(data)
      
    insert_index = len(self.heap_array) - 1 # 가장 마지막에 삽입된 노드의 위치 
    
    while self.checkSorting(insert_index): # True라면 정렬 필요
      parent_index = insert_index // 2
      self.heap_array[insert_index], self.heap_array[parent_index] = self.heap_array[parent_index], self.heap_array[insert_index]
      insert_index = parent_index
      
    return True
  
  def pop(self):
    if len(self.heap_array) <= 1:
      return None
    
    result = self.heap_array[1]
    return result
  
  def sorting(self, popped_index):
    left  = popped_index * 2
    right = popped_index * 2 + 1
    
    if left >= len(self.heap_array): # 좌측 자식노드가 없는 경우 
      return False
    
    elif right >= len(self.heap_array): # 우측 자식노드가 없는 경우 = 좌측 자식노드만 존재
      if self.heap_array[popped_index] < self.heap_array[left]:
        return True # 재정렬 필요 
      else:
        return False # 재정렬 불필요 
      
    else: # 좌/우측 자식노드가 모두 존재 
      if self.heap_array[left] > self.heap_array[right]: # 좌측 자식노드가 우측 자식노드보다 더 크고 
        if self.heap_array[popped_index] < self.heap_array[left]: # 현재 루트노드가 더 작다면  
          return True # 재정렬 필요 
        else:
          return False 
      else:
        if self.heap_array[popped_index] < self.heap_array[right]: # 현재 루트노드가 우측노드보다 더 크다면 
          return True # 재정렬 필요 
        else:
          return False
        
heap = Heap(0)
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
print(heap.heap_array)

  
  
      
    
    
    