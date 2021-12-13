# 백준 단계별 풀이 4단계
# https://www.acmicpc.net/problem/10952
import sys

flag = True
while(flag):
  a, b = map(int, sys.stdin.readline().split())
  if(a != 0 and b != 0):
    print(a + b)
  elif(a == 0 and b != 0):
    print(a + b)
  elif(a != 0 and b == 0):
    print(a + b)
  else:
    flag = False