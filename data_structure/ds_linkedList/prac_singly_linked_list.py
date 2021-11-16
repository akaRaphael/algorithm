class Node():
  def __init__(self, data, next = None):
    self.data = data
    self.next = next
    
class SinglyLinkedList():
  def __init__(self, data):
    self.head = Node(data)
    
  def add(self, data):
    if self.head == None:
      self.head = data
      
    else:
      node = self.head
      while node.next:
        node = node.next
      node.next = Node(data)
      
  def printAll(self):
    node = self.head
    while node:
      print(node.data)
      node = node.next
      
  def delete(self,data):
    if self.head == None:
      print("No exsting nodes")
      return
    
    elif self.head.data == data:
      temp = self.head
      self.head = self.head.next
      del temp
      
    else:
      node = self.head
      while node.next:
        if node.next.data == data:
          temp = node.next
          node.next = node.next.next
          del temp
        else:
          node = node.next
          
singly_list = SinglyLinkedList(0)
singly_list.add(1)
singly_list.add(2)
singly_list.add(3)
singly_list.add(4)
singly_list.add(5)
singly_list.delete(3)
singly_list.printAll()