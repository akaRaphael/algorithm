# 백준 단계별 풀이 8단계
# https://www.acmicpc.net/problem/1011
# t = int(input())
# for _ in range(t):
#   x, y = map(int, input().split())
#   i = 1
#   move = []
#   diff = y - x 
#   while diff > 0:
#     move.append(i)
#     diff = diff - i
#     next = i + 1
#     if diff > next * (next + 1) / 2:
#       i += 1
#     elif diff == next * (next + 1) / 2:
#       move += sorted(move, reverse=True)
#       move.append(1)
#       break
#     else:
#       if i > 1:
#         i -= 1
#       else:
#         i = 1
#   print(len(move))

# 최고속도를 찍는 지점을 찾는다. 이 경우, 세가지 경우가 발생한다. 
# case 1) 최고속도를 찍은 지점까지의 거리와 남은 거리(a, 알파)가 동일한 경우
# case 2) 최고 속도를 찍은 지점까지의 거리 < 남은 거리(a, 알파)의 경우 
# case 2-1) 0 < a <= k인 경우, k속도 만큼 한번 더 간다. 
# case 2-2) k < a <= 2k인 경우, k속도 만큼 두번 더 간다.  
 
# 최고속도 k를 찍는 지점을 찾는 방법은 다음과 같다. 
# 최고속도 k 지점 까지 거리의 합 =  k(k+1)/2
# 최고속도 k 지점 이후 남은 거리의 합 = k(k-1)/2 
# 이 두개의 합을 구하면 k제곱이 나온다. 

t = int(input())
for _ in range(t):
  x, y = map(int, input().split())
  distance = y - x
  k = 0

  while True:
    k += 1
    if distance - k * k <= 0: # 최고 속도 지점을 찾는다. 
      break
  
  if distance - k * k == 0: # case 1
    print(k * 2 - 1)
  else: # case 2
    k = k - 1
    if distance - k * k <= k: #case 2-1
      print(k * 2)
    else: # case 2-2
      print(k * 2 + 1)


