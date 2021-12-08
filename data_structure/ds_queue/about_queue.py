
# 1) Queue 개념 
# - Queue는 한쪽 끝에서는 삽입만 다른 끝에서는 추출만이 수행되는 자료구조다. 
# - FIFO의 순서로 데이터가 정리되어, 가장 먼저 삽입(enqueue)된 데이터가 가장 먼저 추출(dequeue)된다.


# 2) 파이썬에서 Queue 구현하기
# - Queue는 리스트를 이용하여 구현 가능하지만 효율적이지 않다. 
# - 리스트를 사용하면 pop()으로 dequeue를 구현할 수 있지만, 
#   enqueue(새로운 데이터를 맨 앞에 추가)를 위해서는 리스트의 요소를 재정렬 해야하기 때문이다.
# - 그러므로 collections.deque, 파이썬의 Queue 모듈, 연결리스트를 사용하는 것을 권장한다.


# 3) List로 구현하기
# - enqueue의 시간복잡도 O(1)
# - dequeue의 시간복잡도 O(N)
class ListQueue():
  def __init__(self):
    self.queue = []
    
  def enqueue(self, data):
    self.queue.append(data)
    
  def dequeue(self):
    return self.queue.pop(0)
  
  def print_queue(self):
    print(self.queue)
    
  def queue_length(self):
    print(f"queue length = {len(self.queue)}")
  
queue = ListQueue()
queue.enqueue(0)
queue.enqueue(1)
queue.enqueue(2)
queue.print_queue()
queue.queue_length()
queue.dequeue()
queue.print_queue()
queue.queue_length()
