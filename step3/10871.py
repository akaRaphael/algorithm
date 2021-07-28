# 백준 단계별 풀이 3단계 
# https://www.acmicpc.net/problem/10871

n, x = map(int, input().split())
array = list(map(int, input().split()))
for data in array:
  if (data < x):
    print(data, end = ' ')