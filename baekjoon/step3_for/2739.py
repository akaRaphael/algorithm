# 백준 단계별 풀이 3단계 
# https://www.acmicpc.net/problem/2739

dan = int(input())

for i in range(1, 10):
  print("%d * %d = %d" % (dan, i, dan * i))