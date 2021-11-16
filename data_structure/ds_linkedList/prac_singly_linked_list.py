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
    
    elif self.head == data:
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
          
