# 4) collections.deque로 구현하기
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