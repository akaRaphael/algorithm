# 백준 단계별 풀이 9단계 - 택시 기하학
# https://www.acmicpc.net/problem/3053

# 유클리드 기하학 원의 넓이 = PI * r^2
# 택시 기하학 원의 넓이 = 2 * r^2

from math import pi
r = int(input())
print(r ** 2 * pi)
print(2 * r ** 2)