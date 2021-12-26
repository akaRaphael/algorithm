# 프로그래머스 고득점kit 
# stack/queue - 다리를 지나는 트럭 

# bridge_len = 한번에 다리에 오를 수 있는 트럭의 수, 다리를 완전히 지나는데 걸리는 시간 
# weight = 다리가 견딜 수 있는 트럭의 무게 
# truck_weight = 다리를 건너기 위해 대기중인 트럭과 각 트럭의 무게
# * 문제의 핵심은 겹치는 시간을 어떻게 계산할 것인가 

# 내가 풀이한 코드(풀이시간 - 2일, 21.12.25 ~ 21.12.26)
# 비효율 요소 1. on_bridge 생성시간이 input 크기에 비례해서 증가
# 비효율 요소 2. sum(on_bridge)의 연산시간이 input 크기에 비례해서 증가 
def solution(bridge_length, weight, truck_weights):
  answer = 0
  on_bridge = [0] * bridge_length
  while len(on_bridge):
    answer += 1
    on_bridge.pop(0)
    if truck_weights:
      if sum(on_bridge) + truck_weights[0] <= weight:
        on_bridge.append(truck_weights.pop(0))
      else:
        on_bridge.append(0)
  return answer
print(solution(2, 10, [7,4,5,6])) 
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))


# 프로그래머스에서 가장 좋아요를 많이 받은 솔루션 
import collections
DUMMY_TRUCK = 0
class Bridge(object):
  def __init__(self, length, weight):
      self._max_length = length
      self._max_weight = weight
      self._queue = collections.deque()
      self._current_weight = 0

  def push(self, truck):
      next_weight = self._current_weight + truck
      if next_weight <= self._max_weight and len(self._queue) < self._max_length:
          self._queue.append(truck)
          self._current_weight = next_weight
          return True
      else:
          return False

  def pop(self):
      item = self._queue.popleft()
      self._current_weight -= item
      return item

  def __len__(self):
      return len(self._queue)

  def __repr__(self):
      return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()