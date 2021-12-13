# 백준 단계별 풀이 5단계
# https://www.acmicpc.net/problem/10818

n = int(input())
arr = list(map(int, input().split()))
a = min(arr)
b = max(arr)
print(a, b)