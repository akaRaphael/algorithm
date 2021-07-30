# 백준 단계별 풀이 5단계
# https://www.acmicpc.net/problem/3052
import sys

arr = []
for _ in range(10):
  n = int(sys.stdin.readline().strip())%42
  if n not in arr:
    arr.append(n)
print(len(arr))