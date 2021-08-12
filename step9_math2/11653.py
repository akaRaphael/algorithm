# 백준 단계별 풀이 9단계
# https://www.acmicpc.net/problem/11653

n = int(input())
case = []
devider = 2

while n > 1:
  if n % devider == 0:
    case.append(devider)
    n = n / devider
  else:
    devider += 1
    if devider > n:
      break

for i in range(len(case)):
  print(case[i])
