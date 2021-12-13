# 백준 단계별 풀이 5단계
# https://www.acmicpc.net/problem/1546
n = int(input())
arr = list(map(float, input().split()))
maxNum = max(arr)
for i in range(len(arr)):
  arr[i] = arr[i] / maxNum * 100

print(sum(arr) / n)