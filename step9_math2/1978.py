# 백준 단계별 풀이 9단계
# https://www.acmicpc.net/problem/1978

# 소수란 1과 자신으로만 나눠지는 수 
# 즉, 약수가 1과 자신밖에 없는 것

# 어떤 수 n에 대한 약수는 n보다 작다. 
# 즉, 약수 <= n
n = int(input())
case = list(map(int,input().split()))
count = 0

if len(case) == n:
  for i in range(n):
    yaksoo = 0
    for j in range(1, case[i] + 1):
      if case[i] % j == 0:
        yaksoo += 1
    if yaksoo == 2:
      count += 1
print(count)