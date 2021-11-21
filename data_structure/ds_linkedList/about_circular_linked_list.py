# 1) Circular Linked List란?
# - head와 tail이 연결되어 순환구조를 갖는 LinkedList를 말한다.
# - 포인터의 갯수보다 next 포인터가 None값을 가지지 않는다는 것이 특징이다.
# - 즉, 노드가 1개인 경우에도 무한순환하는 Linked List이다. 

# 2) Circular Linked List 구현 

class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
    
class CircularLinkedList():
  def __init__(self, data):
    self.head = Node(data)
    self.head.next = self.head
    
  def add(self, data):
    if self.head:
      curn = self.head
      while curn.next != self.head:
        curn = curn.next 
      
      new_node = Node(data)
      curn.next = new_node
      new_node.next = self.head
    else:
      self.head = Node(data)
      self.head.next = self.head
      
  def removeData(self, data):
    prevn = self.head
    curn = self.head.next
    
    if self.head.data == data:
      # prev 포인터가 없기 때문에, self.head.prev를 찾기위한 과정
      while curn != self.head: 
        prevn = curn
        curn = curn.next
      prevn.next = curn.next
      self.head = curn.next
      return
    
    while curn != self.head:
      if curn.data == data:
        prevn.next = curn.next
        return
      prevn = curn
      curn = curn.next
    return -1 # 지우려는 데이터가 없는 경우 
  
  def removeAt(self, idx):
    if idx == 0:
      if self.head:
        if self.head.next: # head 외 다른 노드가 존재하는 경우 
          curn = self.head.next
          while curn.next != self.head:
            curn = curn.next
          curn.next = self.head.next
          self.head = self.head.next
        else: # head가 유일한 노드인 경우 
          self.head = None
          return 
    else:
      prevn = self.head
      curn = self.head.next
      count = 1
      while curn != self.head:
        if count == idx:
          prevn.next = curn.next
          return
        prevn = curn
        curn = curn.next
        count += 1
      return -1 
    
  def getDataIndex(self, data):
    idx = 0
    curn = self.head
    while curn.next != self.head:
      if curn.data == data:
        print(f"검색한 {data}의 index = {idx}")
        return
      else:
        curn = curn.next
        idx += 1
    return -1 # 데이터를 찾지 못한 경우
  
  def insertAt(self, idx, data):
    new_node = Node(data)
    if self.head:
      if idx == 0:
        curn = self.head.next
        count = 1
        while curn.next != self.head:
          curn = curn.next 
          count += 1
        new_node.next = self.head
        self.head = new_node
        curn.next = self.head
        return
      else:
        prevn = self.head
        curn = self.head.next
        count = 1
        while curn.next != self.head:
          if idx == count:
            prevn.next = new_node
            new_node.next = curn
            return
          else:
            curn = curn.next
            count += 1
    else:
      self.head = new_node
      self.head.next = self.head
      return
    
  def print(self):
    if self.head:
      curn = self.head
      result = ''
      while curn:
        result += str(curn.data)
        if curn.next != self.head:
          result += '=>'
        else:
          break
        curn = curn.next
      print(result)
    else:
      print("Nothing to print out.")

circular = CircularLinkedList(0)
circular.add(1)
circular.add(2)
circular.add(3)
circular.add(4)
circular.print()
circular.insertAt(0,5)
circular.print()
circular.removeAt(0)
circular.print()