# 백준 단계별 풀이 9단계 - 소수
# https://www.acmicpc.net/problem/2581

# m = int(input())
# n = int(input())
# case = []

# for i in range(m, n + 1):
#   yaksoo = 0
#   for j in range(1, i + 1):
#     if i % j == 0: 
#       yaksoo += 1
#       if yaksoo > 2: # 시간 초과를 막기위함.
#         break
#   if yaksoo == 2: 
#     case.append(i)

# if len(case) > 0:
#   print(sum(case))
#   print(min(case))
# else:
#   print(-1)

#############################3

def YaksooList(start, end):
  case = []
  for i in range(start, end + 1):
    yaksoo = 0
    for j in range(1, i + 1):
      if i % j == 0: 
        yaksoo += 1
        if yaksoo > 2: # 시간 초과를 막기위함.
          break
    if yaksoo == 2: 
      case.append(i)
  return case


m = int(input())
n = int(input())
result = YaksooList(m, n)

if len(result) > 0:
  print(sum(result))
  print(min(result))
else:
  print(-1)

