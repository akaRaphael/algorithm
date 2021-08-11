# 백준 단계별 풀이 8단계
# https://www.acmicpc.net/problem/2292
n = int(input()) 
prev = 1
count = 1
while True:
  if prev < n:
    prev = prev + 6 * count
    count += 1

  else:
    print(count)
    break