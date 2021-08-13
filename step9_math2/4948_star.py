# 백준 단계별 풀이 9단계
# https://www.acmicpc.net/problem/4948

def check_sosu(n):
  two_n = 2 * n
  a = [False, False] + [True] * (two_n - 1)
  primes = []

  for i in range(2, two_n + 1):
    if a[i]:
      primes.append(i)
      for j in range(2 * i, two_n + 1, i):
        a[j] = False

  result = []
  for data in primes:
    if data > n:
      result.append(data)

  return result

while True:
  n = int(input())
  if n == 0:
    break
  print(len(check_sosu(n)))