# praticing Stack implementation 
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
      print("Stack underflow")
      exit()

  def size(self):
    return len(self.top)

class Stack1:
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

  def isContain(self, item):
    return item in self.top

  def peek(self):
    if not self.isEmpty():
      return self.top[-1]
    else:
      print("Stack underflow")
      exit()

  def clear(self):
    self.top = []

  def size(self):
    return len(self.top)

class Stack2:
  def __init__(self):
    self.top = []

  def __len__(self):
    return len(self.top)

  def isEmpty(self):
    return len(self.top) == 0

  def push(self, item):
    self.top.append(item)

  def pop(self, item):
    if not self.isEmpty():
      return self.top.pop(-1) 
    else:
      print("Stack underflow")
      exit()

  def peek(self):
    if not self.isEmpty():
      return self.top[-1]
    else:
      print("Stack underflow")
      exit()

  def isContain(self, item):
    return item in self.top

  def clear(self):
    self.top = []

  def size(self):
    return len(self.top)