# 프로그래머스 고득점 kit - Greedy
# 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

# 내가 짠 코드 
# 최소신장트리를 구하는 문제라고 판단함 

def solution(n, costs):
  connected = {}
  total_cost = [0] * n
  
  for idx in range(n):
    connected[idx] = None
  
  for data in costs:
    start = data[0]
    end = data[1]
    cost = data[2]
    
    if connected[start] != None:
      if total_cost[start] > cost:
        connected[start] = end
        total_cost[start] = cost
    else:
      connected[start] = end
      total_cost[start] = cost
    
    if connected[end] != None:
      if total_cost[end] > cost:
        connected[end] = start
        total_cost[end] = cost
    else:
      connected[end] = start
      total_cost[end] = cost
  print(total_cost)
  print(connected)
  return sum(total_cost)
print(solution(n, costs))
      