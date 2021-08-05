# 백준 단계별 풀이 7단계
# https://www.acmicpc.net/problem/5622

# index는 0번 부터 시작인데 알파벳은 2부터 시작이다 = +2초 
# 총 걸리는 시간 = 숫자 + 2초 
# 문자열을 입력 받는다
# 해당 문자에 맞는 번호를 거는데 걸리는 총 시간을 구해라 

dial_s = ["-", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

input_s = input()
result = 0
for char in input_s:
  for i in range(len(dial_s)):
    if dial_s[i].find(char) != -1:
      result += (i + 2)

print(result)

# dial_s = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

# input_s = input()
# result = 0
# for char in input_s:
#   for i in range(len(dial_s)):
#     if dial_s[i].find(char) != -1:
#       result += (i + 3)

# print(result)