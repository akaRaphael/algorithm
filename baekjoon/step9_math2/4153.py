# 백준 단계별 풀이 9단계 - 직각삼각형
# https://www.acmicpc.net/problem/4153

# 내가 생각한 풀이
# 피타고라스의 정리를 이용하여 푼다. 

while True:
  case = list(map(int, input().split()))
  if sum(case) == 0:
    break
  else:
    case.sort()
    if case[0] ** 2 + case[1] ** 2 == case[2] ** 2:
      print("right")
    else:
      print("wrong")