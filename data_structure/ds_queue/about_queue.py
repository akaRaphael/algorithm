
# 1) Queue 개념 
# - Queue는 한쪽 끝에서는 삽입만 다른 끝에서는 추출만이 수행되는 자료구조다. 
# - FIFO의 순서로 데이터가 정리되어, 가장 먼저 삽입(enqueue)된 데이터가 가장 먼저 추출(dequeue)된다.


# 2) 파이썬에서 Queue 구현하기
# - Queue는 리스트를 이용하여 구현 가능하지만 효율적이지 않다. 
# - 리스트를 사용하면 pop()으로 dequeue를 구현할 수 있지만, 
#   enqueue(새로운 데이터를 맨 앞에 추가)를 위해서는 리스트의 요소를 재정렬 해야하기 때문이다.
# - 그러므로 collections.deque, 파이썬의 Queue 모듈, 연결리스트를 사용하는 것을 권장한다.

# 3) Queue 시간복잡도 
# - enqueue =>  O(1)
# - dequeue => O(N)

# 4) Queue의 활용 
#  - CPU 스케쥴링, Disk 스케쥴링
#  - 비동기적으로 데이터가 저장되는 환경에서 이를 순차적으로 처리하기 위해 사용 
#  - 인터럽트의 순차적 처리 

# 5) List를 이용한 Queue
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

# 5) collections.deque를 이용한 Queue
# - deque(데크)는 double-ended queue로 앞/뒤 방향에서 데이터를 처리할 수 있는 양방향 Queue를 의미한다.
# - appendleft()를 사용하면 맨 앞에 데이터를 추가할 수 있다. 
# - popleft()를 사용하면 맨 앞의 데이터를 추출할 수 있다. 
# - 내부적으로 doubly linked list로 구현되어 있기 때문에 빠른 처리가 가능하다. 
# - enqueue / dequeue 의 시간복잡도 O(1)
# * deque를 사용하는 이유 - 자료구조의 시작과 끝부분에서 삽입/삭제가 빈번한 경우, 리스트보다 효율적이다! 

from collections import deque

dq = deque()
dq.append(1)
dq.append(2)
dq.append(3)

# print(dq)
# dq.appendleft(4)
# print(dq)
# print(dq.pop())
# print(dq)
# print(dq.popleft())
# print(dq)

# 6) 파이썬 queue 모듈로 구현하기 
# - 파이썬 queue 모듈은 기본 큐(Queue), 우선순위 큐(PriorityQueue), 스택(LifoQueue)을 제공한다.
import queue
que = queue.Queue()
que.put(1)
que.put(2)
que.put(3)
# print(que.get())
# print(que.get())