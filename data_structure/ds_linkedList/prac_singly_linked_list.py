class Node():
  def __init__(self, data, next = None):
    self.data = data
    self.next = next
    
class SinglyLinkedList():
  def __init__(self, data):
    self.head = Node(data)
    
  def add(self, data):
    if self.head == None:
      self.head = Node(data)
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
    print("\n")
      
  def delete(self, data):
    if self.head == None:
      print("nothing to delete")
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
          
single = SinglyLinkedList(0)
single.printAll()

single.add(1)
single.add(2)
single.add(3)
single.add(4)
single.printAll()

single.delete(0)
single.printAll()
single.delete(3)
single.printAll()
single.delete(4)
single.printAll()