# 프로그래머스 고득점 Kit - DFS/BFS
# 여행경로
# https://programmers.co.kr/learn/courses/30/lessons/43164

# 입출력 예
# tickets	/ return
# [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	/ ["ICN", "JFK", "HND", "IAD"]

# 다른 사람의 솔루션 - https://kyoung-jnn.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-DFS-%EC%8A%A4%ED%83%9D
from collections import defaultdict
def solution(tickets):
  answer = []
  routes = defaultdict(list)

  for ticket in tickets:
    routes[ticket[0]].append(ticket[1])

  for key in routes.keys():
    routes[key].sort(reverse=True)

  stack = ['ICN']
  while stack:
    tmp = stack[-1]

    if not routes[tmp]:
      answer.append(stack.pop())
    else:
      stack.append(routes[tmp].pop())
  answer.reverse()

  return answer