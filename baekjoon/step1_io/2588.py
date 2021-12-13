# 백준 단계별 풀이 1단계 
# https://www.acmicpc.net/problem/2588

a = int(input())
b = list(input())

for i in range(len(b)):
  b[i] = int(b[i])

first = a * b[-1]
second = a * b[-2]
third = a * b[-3]
result = first + second * 10 + third * 100
print(first, second, third, result, sep="\n")