# 백준 단계별 풀이 3단계 
# https://www.acmicpc.net/problem/15552

import sys

n = int(sys.stdin.readline())
for _ in range(n):
  a, b = map(int, sys.stdin.readline().split())
  print(a + b)
