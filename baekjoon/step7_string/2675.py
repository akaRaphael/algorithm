# 백준 단계별 풀이 7단계
# https://www.acmicpc.net/problem/2675

test_case = int(input())

for _ in range(test_case):
  num, s_input = input().split()
  num = int(num)
  result = ''
  for i in range(len(s_input)):
    result += (s_input[i] * num)
  
  print(result)

