# 백준 단계별 풀이 9단계 - 터렛
# https://www.acmicpc.net/problem/1002

# 아무리 생각해봐도 어떻게 접근해야하는지 모르겠다.
# 그래서 해답을 찾아보았다. 

# approach - 기하학의 원과 원의 접점의 개수를 구하는 방법을 사용한다. 
# 입력값 x, y는 원의 중심 좌표를, r은 원의 반지름을 의미한다. 

# 두 원의 중심 사이의 거리는 피타고라스의 정리를 이용하여 구한다. 

# 두 원의 접점이 생길 수 있는 경우의 수 (https://mathbang.net/101)
# 1. 두 원의 중심이 같은 경우 == r1, r2, d가 모두 동일한 경우 
#   => 접점이 무한개

# 2. 두 원이 서로 멀리 떨어져 있음 == r1, r2, d 중 가장 큰 수가 나머지 두 수의 합보다 큰 경우 
#   => 접점이 0개 

# 3. 두 원의 접점이 1개인 경우 
#   => 외접점 1개(두개의 원이 한점에 맞닿음) == r1, r2의 합이 d와 같다
#   => 내접점 1개 (하나의 원 안에 다른 원이 있고 한 점에서 내접함) == r1, r2의 차가 d와 같다

# 4. 두 원의 접점이 2개인 경우
#   => 두 원이 부분적으로 겹쳐서 2개의 접점이 생김 
#   => 위의 3가지 경우를 제외한 마지막 경우의 수 

from math import sqrt

t = int(input())

for _ in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  distance = sqrt((x2-x1) ** 2 + (y2 - y1) ** 2) # 피타고라스의 정리

  if x1 == x2 and y1 == y2: 
    if r1 == r2: # 접점이 무한개
      print(-1)
    else: # 중심은 같으나 접점이 0개 (원 안에 원이 있는데 접점이 없음)
      print(0)
  
  else:
    if r1 > distance + r2 or r2 > distance + r1 or distance > r1 + r2: # 두 원이 멀리 떨어져 있음 == 접점 0개
      print(0)
    elif abs(r1 - r2) == distance or r1 + r2 == distance: # 내접 또는 외접의 경우 
      print(1)
    else: # 남은 경우의 수는 접점이 2개인 경우 
      print(2) 