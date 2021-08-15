# 파이썬 50제 (1 ~ 50) - 화성수학
# https://www.acmicpc.net/problem/5355

from sys import stdin

t = int(input())
for _ in range(t):
  a = list(stdin.readline().split())
  result = 0
  for data in a:
    if data == "@":
      result *= 3
    elif data == "%":
      result += 5
    elif data == "#":
      result -= 7
    else:
      result += float(data)
  print('%.2f' % result)
