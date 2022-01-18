# 프로그래머스 고득점 Kit - DFS/BFS
# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

# 입출력 예
# n	computers	return
# 3	/ [[1, 1, 0], [1, 1, 0], [0, 0, 1]] /	2
# 3	/ [[1, 1, 0], [1, 1, 1], [0, 1, 1]] /	1
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

# dfs를 사용한 풀이법 
def solution(n, computers):
  visited = [False] * n
  answer = 0
  
  for start in range(0, n):
    if visited[start] == False:
      dfs(n, computers, start, visited)
      answer += 1
      
  return answer

def dfs(n, computers, start, visited):
  visited[start] = True
  for i in range(n):
    if visited[i] == False and computers[start][i] == 1:
      visited = dfs(n, computers, i, visited)
  return visited

print(solution(n, computers))


# bfs를 이용한 풀이 
def solution2(n, computers):
  answer = 0
  visited = [False] * n
  for com in range(n):
    if visited[com] == False:
      bfs(n, computers, com, visited)
      answer += 1
  return answer

def bfs(n, computers, com, visited):
  visited[com] = True
  queue = []
  queue.append(com) 
  while len(queue) != 0:
    com = queue.pop(0)
    visited[com] = True
    for connect in range(n):
      if connect != com and computers[com][connect] == 1:
        if visited[connect] == False:
          queue.append(connect)
          
print(solution2(n, computers))