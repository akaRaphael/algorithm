# 백준 단계별 풀이 8단계
# https://www.acmicpc.net/problem/2775

# a 층 b호에 사는 경우, a-1층의 1호 부터 b호 까지의 사람 수 의 합만큼 살아야 한다. 
# 아파트는 0층부터 있다. 
# 0층의 i호는 i명의 사람이 산다.
# 305호의 명수 = 304호 명수 + 205호의 명수 
t = int(input())
for _ in range(t):
  floor = int(input())
  room = int(input())
  apart = [ i for i in range(1, room + 1)]
  for _ in range(floor):
    for j in range(1, room):
      apart[j] += apart[j - 1]
  print(apart[-1])