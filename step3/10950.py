# 백준 단계별 풀이 3단계 
# https://www.acmicpc.net/problem/10950

import sys

n = int(input())
for _ in range(n):
  a, b = map(int, sys.stdin.readline().split() )
  print(a + b)