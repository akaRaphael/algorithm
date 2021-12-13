# 백준 단계별 풀이 5단계
# https://www.acmicpc.net/problem/2562
import sys

n = 9
arr = []

for _ in range(n):
  arr.append(int(sys.stdin.readline()))

print(max(arr))
print(arr.index(max(arr)) + 1)