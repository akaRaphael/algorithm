# practicing doubly linked list implementation

class Node():
  def __init__(self, data, prev = None, next = None):
    self.data = data
    self.prev = prev
    self.next = next

class DoublyLinkedList():
  def __init__(self, data):
    self.head = Node(data)
    self.tail = self.head
    
  def insert(self, data):
    if self.head:
      node = self.head
      while node.next:
        node = node.next
      new_node = Node(data)  
      node.next = new_node
      new_node.prev = node
      self.tail = new_node 
    else:
      self.head = Node(data)
      self.tail = self.head
  
  def insertAt(self, idx, data):
    if self.head:
      if idx == 0:
        temp = self.head
        new_node = Node(data)
        self.head = new_node
        new_node.next = self.head.next
        del temp
      else: 
        node = self.head
        count = 0
        while node:
          node = node.next
          count += 1
          if count == idx:
            new_node = Node(data)
            node.prev.next = new_node
            new_node.next = node
            new_node.prev = node.prev
            node.prev = new_node
  def delete(self):
    if self.head:
      node = self.head
      while node.next:
        node = node.next
      temp = node
      if self.head != self.tail:
        self.tail = node.prev
        self.tail.next = None
        del node
      else:
        self.head = None
        self.tail = None
        print("Nothing to delete")   
  
  def deleteAt(self, idx):
    if self.head:
      node = self.head
      if idx == 0:
        self.head = node.next
        del node
      else:
        count = 0
        while node.next:
          node = node.next
          count += 1
          if count == idx:
            temp = node
            node.prev.next = node.next
            node.next.prev = node.prev
            del temp
        # print(f"head = {self.head.data}")
        # print(f"tail = {self.tail.data}")
        
  def searchFromHead(self, data):
    if self.head:
      node = self.head
      count = 0
      while node:
        if node.data == data:
          print(f"앞에서 {count}번째 노드입니다. ==> {data}")
          break
        else:
          node = node.next
          count += 1
    else:
      print("Nothing to search from head")
      return
    
  def searchFromTail(self, data):
    if self.tail:
      node = self.tail
      count = 0
      while node:
        if node.data == data:
          print(f"뒤에서 {count}번째 노드입니다. ==> {data}")
          break
        else:
          node = node.prev
          count += 1
    else:
      print("Nothing to search from tail")
      return
        
  def printAll(self):
    if self.head:
      node = self.head
      while node:
        print(node.data)
        node = node.next
      print("\n")
    else:
      print("Nothing to print")

doubly = DoublyLinkedList(0)
doubly.insert(1)
doubly.insert(2)
doubly.insert(3)
doubly.printAll()
doubly.insertAt(1, 10)
doubly.printAll()
doubly.searchFromHead(2)
doubly.searchFromTail(1)
doubly.delete()
doubly.printAll()
doubly.deleteAt(1)
doubly.printAll()
doubly.delete()
doubly.delete()
doubly.delete()
doubly.printAll()
doubly.searchFromHead(2)
doubly.searchFromTail(1)
