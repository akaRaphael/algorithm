# 파이썬 50제 (1 ~ 50) - 저작권 
# https://www.acmicpc.net/problem/2914

from math import ceil
a, b = map(int, input().split())
multiple = a * b
result = 0

while True:
  if int(multiple / a) == b - 2:
    result = multiple
    break
  else:
    multiple -= 1

while True:
  if ceil(multiple / a) == b:
    print(multiple)
    break
  else:
    multiple += 1

################## 개선된 코드 
a, b = map(int, input().split())
print(a * (b - 1) + 1)