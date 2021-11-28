class Node():
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BST():
  def __init__(self, data):
    self.head = Node(data)
    
  def insert(self, data):
    self.curn = self.head
    while True:
      if data < self.curn.data:
        if self.curn.left != None:
          self.curn = self.curn.left
        else:
          self.curn.left = Node(data)
          break
      else:
        if self.curn.right != None:
          self.curn = self.curn.right
        else:
          self.curn.right = Node(data)
          break
  
  def search(self, data):
    self.curn = self.head
    while self.curn:
      if self.curn.data == data:
        print(f"{data} is in the BST")
        return
      elif data < self.curn.data:
        self.curn = self.curn.left
      else:
        self.curn = self.curn.right
    print(f"{data} was not found")
  
  def delete(self, data):
    self.curn = self.head
    self.parent = self.head
    searched = False
    
    while self.curn:
      if self.curn.data == data:
        searched = True
        print(f"{data} is found and deleted")
        return
      
      elif data < self.curn.data:
        self.parent = self.curn
        self.curn = self.curn.left
        
      else:
        self.parent = self.curn
        self.curn = self.curn.right
        
    if searched == False:
      print(f"{data} was not found")
    
    else:
      if self.curn.left == None and self.curn.right == None:
        if data < self.parent.data:
          self.parent.left = None
        else:
          self.parent.right = None
          
        del self.curn
        
      elif self.curn.left != None and self.curn.right == None:
        if data < self.parent.data:
          self.parent.left = self.curn.left
        else:
          self.parent.right = self.curn.left
          
      elif self.curn.left == None and self.curn.right != None:
        if data < self.parent.data:
          self.parent.left = self.curn.right
        else:
          self.parent.right = self.curn.right 
  
        
bst = BST(0)
bst.insert(1)
bst.search(0)
bst.search(1)
bst.search(3)
bst.delete(1)
bst.delete(1)
          
          
      
      
