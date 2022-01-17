# 프로그래머스 고득점 kit - 이분탐색 
# 징검다리
# https://programmers.co.kr/learn/courses/30/lessons/43236

# 입출력 예
# distance / rocks / n / return
# 25 / [2, 14, 11, 21, 17] / 2 / 4
distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2

# 다른사람의 풀이 
# 1) 기준 설정 
# 중간 값 = 찾는 값 = 돌 사이의 거리 중 최소값이라고 가정한다. 
# 시작지점 = 최소 값 = 시작지점 = 0 
# 종료지점 = 최대 값 = distance

# 2) 로직 
# - 돌 사이의 거리를 구했을 때, mid값 보다 작은 돌은 제거한다. 
#   제거된 돌이 n보다 많다면 mid 값이 너무 크다는 의미다. 
#   그러므로 mid 값을 감소시킨다. 

# - 돌 사이의 거리를 구했을 때, mid값 보다 거리가 큰 돌은 놔둔다.
#   제거된 돌이 n보다 작다면 mid 값이 너무 작다는 의미다.  
#   그러므로 mid 값을 증가시킨다. 

def solution(distance, rocks, n):
  answer = 0
  start = 0
  end = distance
  rocks.sort() # 오름차순 정렬 
  
  while start <= end:
    mid = (start + end) // 2 # 중간 값
    del_stones = 0 # 제거한 돌의 수 
    curn_stone = 0 # 기준 돌(시작지점) 
    
    for rock in rocks:
      if rock - curn_stone < mid: # 돌 사이의 거리가 중간 값보다 작으면 제거 
        del_stones += 1
        
      else: # 중간 값보다 큰 경우, 해당 돌이 기준이 된다. 
        curn_stone = rock
        
      if del_stones > n: # 제거된 돌의 수가 조건보다 많은 경우 
        break
      
    if del_stones > n: # 제거된 돌이 너무 많으면 중간 값이 크다는 의미로 탐색 범위를 작은 쪽으로 한다.
      end = mid - 1
    else: # 제거된 될이 너무 적으면 중간 값보다 작다는 의미로, 탐색 범위를 큰 쪽으로 한다.
      answer = mid
      start = mid + 1
  return answer
      
print(solution(distance, rocks, n))