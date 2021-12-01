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
      if data == self.curn.data:
        print(f"{data} is in BST")
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
    
    while True:
      if data == self.curn.data:
        searched = True
        break
      
      elif data < self.curn.data:
        self.parent = self.curn
        self.curn = self.curn.left
        
      else:
        self.parent = self.curn
        self.curn = self.curn.right
        
    if searched == False:
      print(f"{data} is not in BST")
      return
    
    # case 1
    if self.curn.left == None and self.curn.right == None:
      if data < self.parent.data:
        self.parent.left = None
      else:
        self.parent.right = None
        
    # case 2  
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
        
    # case 3  
    elif self.curn.left != None and self.curn.right != None:
      if data < self.parent.data:
        self.change_node = self.curn.right
        self.change_parent = self.curn.right
        
        while self.change_node.left != None:
          self.change_parent = self.change_node
          self.change_node = self.change_node.left
          
        self.change_parent.left = None
        
        if self.change_node.right != None:
          self.change_parent.left = self.change_node.right
        else:
          self.change_parent.left = None
          
        self.parent.left = self.change_node
        self.change_node.right = self.curn.right
        self.change_node.left = self.curn.left
        
    else:
      self.change_node = self.curn.right
      self.change_parent = self.curn.right
      
      while self.change_node.left != None:
        self.change_parent = self.change_node
        self.change_node = self.change_node.left 
        
      if self.change_node.right != None:
        self.change_parent.left = self.change_node.right
        
      else:
        self.change_parent.left = None
        
      self.parent.right = self.change_node
      self.change_node.left = self.curn.left
      self.change_node.right = self.curn.right
      
    return True