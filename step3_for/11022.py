# 백준 단계별 풀이 3단계 
# https://www.acmicpc.net/problem/11022
import sys

n = int(input())
for i in range(1, n+1):
  a, b = map(int, sys.stdin.readline().split())
  print("Case #%d: %d + %d =" % (i, a, b), a + b)