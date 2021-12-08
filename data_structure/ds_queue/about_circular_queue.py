# Circular Queue란?
# - 순환하는 형태를 가진 Queue
# - 예를 들어 [1,2,3,4] 라는 Queue가 있는 경우, 
# - pop을 통해 1과 2를 추출하면 [None, None, 3, 4]의 위치로 Queue가 형성된다. 
# - 이때 head = 3, tail = 4가 되는 것이다. 
# - 새로운 요소 6이 추가되는 경우, Queue는 [6, None, 3, 4]의 형태를 갖는다.
# - 이때 head = 3, tail = 6이 된다. 
# - enqueue를 할 때 tail의 위치가 변경되며, dequeue를 할 때 head의 위치가 변경된다. 

class Cqueue():
  def __init__(self, length):
    self.length = length
    self.queue = [None] * length
    self.head = self.tail = -1 
    
  def enqueue(self, data):
    if (self.tail + 1) % self.length == self.head:
      print("The circular queue is full.")
      return
    elif self.head == -1:
      self.head = 0
      self.tail = 0
      self.queue[self.tail] = data
    else:
        self.tail = (self.tail + 1) % self.length
        self.queue[self.tail] = data 
        
  def dequeue(self):
    if self.head == -1:
      print("The circular queue is empty.")
    elif self.head == self.tail:
      temp = self.queue[self.head]
      self.queue[self.head] = None
      self.head = -1
      self.tail = -1
      return temp
    else:
      temp = self.queue[self.head]
      self.queue[self.head] = None
      self.head = (self.head + 1) % self.length
      return temp
    
  def printCqueue(self):
    if self.head == -1:
      print("The circular queue is empty.")
    
    elif self.tail >= self.head:
      for i in range(self.head, self.tail + 1):
        print(f"[{self.queue[i]}]", end = "")
      print()
    
    else:
      for i in range(self.head, self.length):
        print(f"[{self.queue[i]}]", end = "")
      for i in range(0, self.tail + 1):
        print(f"[{self.queue[i]}]", end = "") 
      print()
      
  def printRare(self):
    print(f"head = {self.head}")
    print(f"tail = {self.tail}")
    print(self.queue) 
    print()

cqueue = Cqueue(5)
cqueue.enqueue(0)
cqueue.enqueue(1)
cqueue.enqueue(2)
cqueue.enqueue(3)
cqueue.enqueue(4)
cqueue.printRare()
cqueue.dequeue()
cqueue.printRare()
cqueue.enqueue(5)
cqueue.printRare()
cqueue.dequeue()
cqueue.printRare()

    
        
    
      