# Deque implementation in python

class Deque():
    def __init__(self):
        self.deque = []
    
    def isEmpty(self):
        if len(self.deque) == 0:
            print("deque is empty.")
        else:
            print("deque is not empty.")
            
    def insertEnd(self, data):
        self.deque.append(data)
        
    def insertFront(self, data):
        self.deque.insert(0, data)
        
    def removeFront(self):
        return self.deque.pop(0)
    
    def removeEnd(self):
        return self.deque.pop()
    
    def size(self):
        print(f"length = {len(self.deque)}")
        
    def printDeque(self):
        print(self.deque)
        
deque = Deque()
deque.isEmpty()
deque.insertEnd(1)
deque.insertFront(0)
deque.size()
deque.printDeque()