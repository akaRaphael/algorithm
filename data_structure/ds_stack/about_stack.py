# 1) Stack 이란?
# Stack은 LIFO 규칙을 갖는 자료구조다.
# 맨 처음 들어온 데이터가 가장 마지막 순서에 적재된다.
# 가장 마지막에 들어온 데이터가 가장 첫번째 순서에 적재된다.  

# 2) Stack의 성질 
# Stack은 데이터를 삽입할 때, push() / 데이터를 추출할 때, pop()을 사용한다.
# 파이썬에서는 리스트를 이용하여 stack을 구현한다. 
# 파이썬에서는 push 대신 append를 사용한다. 
# pop()을 사용하면 원소가 추출되면서 동시에 제거된다. 
# 그러므로 단순히 원소를 가져오기만 하고 싶다면 stack[-1]을 사용한다.  

# 3) Stack 구현 

class Stack:
  def __init__(self):
    self.top = [] 

  def __len__(self):
    return len(self.top)

  def __str__(self):
    return str(self.top[::1])

  def push(self, item):
    self.top.append(item)
  
  def isEmpty(self):
    return len(self.top) == 0

  def pop(self):
    if not self.isEmpty():
      return self.top.pop(-1)
    else:
      print("Stack underflow")
      exit()
  
  def clear(self):
    self.top = []

  def isContain(self, item):
    return item in self.top

  def peek(self):
    if not self.isEmpty():
      return self.top[-1]
    else:
      print("underflow")
      exit()

  def size(self):
    return len(self.top)