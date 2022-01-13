# 프로그래머스 고득점 kit - Greedy
# 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861

import graphlib
from tkinter import N


n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

# 내가 짠 코드 
# 최소신장트리를 구하는 문제라고 판단함 
# 크루스칼 알고리즘을 사용하여 구현해보자.



# 다른 사람의 풀이 
def solution(n, costs):
  answer = 0
  costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬
  connect = set([costs[0][0]]) # 연결을 확인하는 집합

  # Kruskal 알고리즘으로 최소 비용 구하기
  while len(connect) != n:
      for cost in costs:
          if cost[0] in connect and cost[1] in connect:
              continue
          if cost[0] in connect or cost[1] in connect:
              connect.update([cost[0], cost[1]])
              answer += cost[2]
              break
              
  return answer