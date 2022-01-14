# 프로그래머스 고득점 kit - Greedy
# 단속 카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884

# 입출력 예
# routes / return
# [[-20,-15], [-14,-5], [-18,-13], [-5,-3]] / 2

# 내가 생각한 풀이법 
# - 모든 차량이 무조건 한번은 단속 카메라를 거치기 위해서는 
#   모든 차량이 공통적으로 지나는 route를 찾아야 한다. 
# - 공통 루트를 찾고, 예외케이스를 찾아서 이 두 곳에 설치하면 된다.


routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

# 다른 사람의 풀이 
def solution(routes):
  answer = 0 
  
  # 1. 진출지점을 기준으로 오름차순 정렬 
  routes.sort(key = lambda x:x[1])
  
  # 2. 최대 -30000이므로 초기 카메라 위치를 -30001로 설정
  camera = -30001
  
  # 3. routes의 요소를 반복하면서 camera의 진입지점이 route[0]보다 작은지 확인
  # - 만약 작다면, 현재 카메라 위치를 만나지 못하므로 카메라를 추가하고, 
  #   가장 최근 카메라 위치를 route[1]로 갱신한다.
  
  for route in routes:
    if camera < route[0]:
      answer += 1
      camera = route[1]
  return answer

print(solution(routes))