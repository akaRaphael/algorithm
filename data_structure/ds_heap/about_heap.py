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
  def __init__(self,data):
    self.heap_array = list()
    self.heap_array.append(None)
    self.heap_array.append(data)
    
  def move_up(self, insert_index): # 부모노드 < 자식노드 경우를 검증 (삽입시 사용)
    if insert_index <= 1:
      return False
    else:
      parent_index = insert_index // 2
      if self.heap_array[insert_index] > self.heap_array[parent_index]:
        return True
      else:
        return False
  
  def insert(self, data):
    if len(self.heap_array) == 0: # heap 객체에 데이터가 없는 경우 
      self.heap_array.append(None)
      self.heap_array.append(data)
      return True
    
    # heap 객체에 데이터가 있는 경우 
    self.heap_array.append(data)
    insert_index = len(self.heap_array) - 1 # 방금 삽입된 data의 위치 찾기
    
    while self.move_up(insert_index):
      parent_index = insert_index // 2
      self.heap_array[parent_index], self.heap_array[insert_index] = self.heap_array[insert_index], self.heap_array[parent_index]
      insert_index = parent_index
      
    return True
      
  def move_down(self, pop_index): # 부모노드 < 자식노드 경우를 검증(삭제시 사용)
    left_child = pop_index * 2
    right_child = pop_index * 2 + 1
    
    # case1) root의 좌측 자식노드가 없는 경우 
    # - 배열의 길이보다 좌측자식노드의 index가 크거나 같을 수 없다. 즉, 존재하지 않는 index 
    if left_child >= len(self.heap_array): 
      return False # 재정렬 불필요 
    
    # case2) root의 우측 자식노드가 없는 경우 = 좌측노드만 존재하는 경우 
    elif right_child >= len(self.heap_array): 
      # 삭제된 root 자리에 들어간 마지막 노드가 자식노드보다 작은경우 
      if self.heap_array[pop_index] < self.heap_array[left_child]:
        return True # 재정렬 필요
      else:
        return False # 현재 root의 값이 root의 자식노드보다 큰 경우, 재정렬 불필요 
      
    # case3) root의 좌/우측 자식노드가 모두 존재하는 경우 
    else:
      if self.heap_array[left_child] > self.heap_array[right_child]: # 좌측 자식노드 > 우측 자식노드
        if self.heap_array[pop_index] < self.heap_array[left_child]: # 현재 root노드 < 좌측 자식노드 
          return True
        else:
          return False
      else: # 좌측 자식노드 < 우측 자식노드 
        if self.heap_array[pop_index] < self.heap_array[right_child]: # 현재 root노드 < 우측 자식노드 
          return True
        else:
          return False
  
  def pop(self):
    if len(self.heap_array) <= 1:
      return None
    
    return_data = self.heap_array[1] # 루트노드를 지역변수에 저장 
    self.heap_array[1] = self.heap_array[-1] # 마지막 노드를 루트노드로 설정 (재정렬 준비)
    del self.heap_array[-1] # 현재 루트노드에 위치한 마지막 노드를 삭제 
    
    pop_index = 1
    while self.move_down(pop_index):
      left_child = pop_index * 2
      right_child = pop_index * 2 + 1
      
      # 우측 자식노드가 없는 경우 = 좌측 자식노드만 존재하는 경우
      if right_child >= len(self.heap_array):
        if self.heap_array[pop_index] < self.heap_array[left_child]:
          self.heap_array[pop_index], self.heap_array[left_child] = self.heap_array[left_child], self.heap[pop_index]
          pop_index = left_child
          
      else: # 좌우측 자식노드가 모두 존재하는 경우 
        if self.heap_array[left_child] > self.heap_array[right_child]:
          if self.heap_array[pop_index] < self.heap_array[left_child]:
            self.heap_array[pop_index], self.heap_array[left_child] = self.heap_array[left_child], self.heap_array[pop_index]
            pop_index = left_child
        else:
          if self.heap_array[pop_index] < self.heap_array[right_child]:
            self.heap_array[pop_index], self.heap_array[right_child] = self.heap_array[right_child], self.heap_array[pop_index]
            pop_index = right_child
    return return_data
        
heap = Heap(15)
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
heap.insert(20)
print(heap.heap_array)
heap.insert(19)
print(heap.heap_array)
