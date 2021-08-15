# 파이썬 50제 (1 ~ 50) - 인공지능시계
# https://www.acmicpc.net/problem/2530

h, m, s = map(int, input().split())
d = int(input())

s += d % 60
d = d // 60 # ==> d = 분
if s >= 60:
  m += 1
  s -= 60

m += d % 60
d = d // 60 # ==> d = 시간 
if m >= 60:
  h += 1
  m -= 60

h += d % 24
if h >= 24:
  h -= 24

print(h, m, s)
