# 파이썬 50제 (50 ~ 100) - 얼마
# https://www.acmicpc.net/problem/9325

from sys import stdin
input = stdin.readline # 이런식으로 input을 사용할 수 있다.

t = int(input())
for _ in range(t):
  price = int(input())
  option = int(input())
  for _ in range(option):
    a, b = map(int, input().split())
    price += a * b
  print(price)