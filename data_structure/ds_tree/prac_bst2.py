class Node():
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None
    
class BST():
  def __init__(self, data):
    self.head = Node(data)
    
  