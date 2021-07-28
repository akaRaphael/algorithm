# 백준 단계별 풀이 3단계 
# https://www.acmicpc.net/problem/2439

n = int(input())
star = "*"
space = " "
for i in range(1, n+1):
  if (i == n):
    print(star * i)
  else:
    print(space * (n - i-1),star * i)