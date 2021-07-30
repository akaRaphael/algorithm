# 백준 단계별 풀이 2단계 
# https://www.acmicpc.net/problem/2884

H, M = map(int, input().split())

if (M < 45):
  M = M + 15
  if(H > 0):
    print(H-1, M)
  else:
    H = 23
    print(H, M)
else:
    print(H, M-45)