# 백준 단계별 풀이 7단계
# https://www.acmicpc.net/problem/11720

n = int(input())
s_input = input()
result = 0

for i in range(n):
  result += int(s_input[i])

print(result)
