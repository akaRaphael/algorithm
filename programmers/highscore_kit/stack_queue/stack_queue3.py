# 프로그래머스 고득점kit 
# stack/queue - 다리를 지나는 트럭 

# bridge_len = 한번에 다리에 오를 수 있는 트럭의 수, 다리를 완전히 지나는데 걸리는 시간 
# weight = 다리가 견딜 수 있는 트럭의 무게 
# truck_weight = 다리를 건너기 위해 대기중인 트럭과 각 트럭의 무게

# * 문제의 핵심은 겹치는 시간을 어떻게 계산할 것인가 
#   => 모든 단계를 세분화하여 과정 하나당 무조건 1초씩 시간이 증가하도록 한다. 

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


# 다른 풀이법 (deque)
# - list를 사용하면 pop할 때마다 재정렬을 해야한다. 
# - 재정렬 하는 비용을 절약하기 위해 deque를 사용해서 구현해본다. 
from collections import deque

def solution2(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    on_bridge = deque([0 for _ in range(bridge_length)])
    time = 0 
    bridge_weight = 0 
    
    while len(on_bridge) != 0:
        out = on_bridge.popleft()
        bridge_weight -= out
        time += 1
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge_weight += truck
                on_bridge.append(truck)
            else:
                on_bridge.append(0)
    return time

print(solution2(2, 10, [7,4,5,6])) 
print(solution2(100, 100, [10]))
print(solution2(100, 100, [10,10,10,10,10,10,10,10,10,10]))