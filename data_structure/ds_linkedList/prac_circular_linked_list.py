class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
    
class Circular():
  def __init__(self, data):
    self.head = Node(data)
    self.head.next = self.head
    
  def insert(self, data):
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
      
  def insertAt(self, idx, data):
    if self.head:
      prevn = self.head
      curn = self.head.next
      new_node = Node(data)
      if idx == 0:
        while curn.next != self.head:
          curn = curn.next
        new_node.next = self.head
        curn.next = new_node
        self.head = new_node
      
      else:
        count = 1
        while curn.next != self.head:
          if idx == count:
            prevn.next = new_node
            new_node.next = curn
            return #return 또는 break 없으면 while이 안끝남
          else:
            prevn = curn
            curn = curn.next
            count += 1
  
  def removeEnd(self):
    if self.head:
      prevn = self.head
      curn = self.head.next
      while curn.next != self.head:
        prevn = curn
        curn = curn.next
      prevn.next = self.head      
      del curn
    else:
      print("nothing to delete")
      
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
      print("nothing to print")
  
  def removeAt(self, idx):
    if self.head:
      curn = self.head.next
      if idx == 0:
        while curn.next != self.head:
          curn = curn.next
        curn.next = self.head.next
        self.head = self.head.next
      else:
        prevn = self.head
        count = 1
        while curn.next != self.head:
          if idx == count:
            prevn.next = curn.next
            del curn
            return
          else:
            prevn = curn
            curn = curn.next
            count += 1
        
circular = Circular(0)
circular.insert(1)
circular.insert(2)
circular.insert(3)
circular.insert(4)
circular.print()
circular.insertAt(0,5)
circular.print()
circular.insertAt(2,11)
circular.print()
circular.removeAt(0)
circular.print()
circular.removeAt(1)
circular.print()
