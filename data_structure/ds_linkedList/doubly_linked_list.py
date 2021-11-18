# 1) Doubly Linked List 란?
# - 단일연결리스트는 다음 노드의 위치를 안내하는 포인터를 1개 가지고 있다.
# - 이중연결리스트는 이전 노드와 다음 노드의 위치를 안내하는 포인터를 2개 가지고 있다.

# 2) Doubly Linked List의 특징 
# - 단일연결리스트는 역순으로 노드를 탐색하는 것이 불가능 했다. 이전 노드의 위치를 모르기 때문이다.
# - 반면에 이중연결리스트는 역순으로 노드를 탐색할 수 있다. 이전 노드의 위치를 알기 때문이다.

# 3) Doubly Linked List의 장점
# - 각 노드를 기준으로 이전/다음 노드의 위치를 알기 때문에, 특정 노드를 기준으로 새로운 노드를 삽입할 수 있다. 

# 4) Doubly Linked List의 단점
# - 이중연결리스트는 각 노드마다 포인터가 2개 필요하기 때문에 단일연결리스트보다 메모리 공간을 더 필요로한다.


# 5) Doubly Linked List 구현
class Node(object):
  def __init__(self, data, prev = None, next = None):
    self.data = data
    self.prev = prev
    self.next = next
    
class DoublyLinkedList():
  def __init__(self, data):
    self.head = Node(data)
    self.tail = self.head
    
  def add(self, data):
    if self.head == None:
      self.head = Node(data)
      self.tail = Node(data)
    else:
      node = self.head
      while node.next:
        node = node.next
      new_node = Node(data)
      node.next = new_node
      new_node.prev = node
      self.tail = new_node
      
  def printAll(self):
    if self.head:
      node = self.head
      while node:
        print(node.data)
        node = node.next
      print("\n")
    else:
      print("Nothing to print out.")
    
  def insertAt(self, data, idx):
    prevn = None
    nextn = None
    
    if idx == 0:
      new_node = Node(data)
      nextn = self.head
      self.head = new_node
      self.head.next = nextn
      nextn.prev = self.head
        
    else:
      node = self.head
      cur_idx = 0
      while node:
        node = node.next
        cur_idx += 1
        if cur_idx == idx:
          new_node = Node(data)
          temp = node.next 
          node.next = new_node
          new_node.prev = node
          new_node.next = temp
          temp.prev = new_node
          
  def getLength(self):
    count = None
    if self.head:
      node = self.head
      count = 0
      while node:
        node = node.next 
        count += 1
      return count    
    else:
      return count
  
  def searchFromHead(self, data):
    if self.head.data == data:
      print("검색한 데이터는 head 입니다 =>", self.head.data)
      return
    else:
      node = self.head
      count = 0 
      while node:
        node = node.next
        count += 1
        if node.data == data:
          print(f"앞에서 {count}번째 노드입니다 => {node.data}")
          return
        
  def searchFromTail(self, data):
    if self.tail.data == data:
      print(f"검색한 데이터는 tail 입니다 => {self.head.data}")
      return
    else:
      node = self.tail
      count = 0 
      while node.prev:
        node = node.prev
        count += 1
        if node.data == data:
          print(f"뒤에서 {count}번째 노드입니다 => {node.data}")
          return
          
  def delete(self):
    try:
      if self.head:
        node = self.tail
        self.tail = node.prev
        self.tail.next = None
        del node
        
      else:
        print("Nothing to delete")
        
    except:
      self.head = None
      print("Nothing to delete")
      return
    
  def deleteAt(self, idx):
    if self.head:
      if idx == 0:
        node = self.head
        self.head = node.next
        node.next.prev = None
        self.head.next = node.next.next
        del node
        return
      else:
        node = self.head
        count = 0
        while node.next:
          node = node.next
          count += 1
          if count == idx:
            temp = node
            node.prev.next = node.next
            node.next.prev = node.prev
            del temp
            return
                    

doubly = DoublyLinkedList(0)
doubly.add(1)        
doubly.add(2)        
doubly.add(3)        
doubly.add(4)
doubly.insertAt(10, 2)
doubly.printAll()
print(f"length = {doubly.getLength()}")
doubly.searchFromHead(10)
doubly.printAll()
doubly.searchFromTail(0)
doubly.printAll()
doubly.deleteAt(0)
doubly.printAll()
doubly.delete()
doubly.printAll()
doubly.deleteAt(1)
doubly.printAll()
doubly.delete()
doubly.delete()
doubly.delete()
doubly.printAll()
