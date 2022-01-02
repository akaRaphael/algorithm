# 프로그래머스 고득점 kit - heap
# 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627

import itertools
jobs = [[0, 3], [1, 9], [2, 6]]

# 내가 짠 코드 
# - itertools.permutations를 사용하여 모든 조합을 구한다 
# - 시간 측정 메소드를 만들어, 각 케이스의 시간을 측정한다.
# - 측정된 시간을 리스트에 모두 보관한다.
# - 리스트에서 최소값을 뽑아 return한다.
# ==> 예제 케이스는 통과했으나, 테스트케이스는 시간초과로 실패
# ==> 심지어 시간초과가 안나는데도 틀린 케이스가 존재했다. 

def calculate_time(case):
    time = []
    real_time = []
    for idx, job in enumerate(case):
        request_t = job[0]
        process_t = job[1]
        time.append(process_t)
        if idx == 0:
            real_time.append(process_t)
        else:
            real_time.append(sum(time) - request_t)
    avg_time = int(sum(real_time) / len(jobs))
    return avg_time

def solution(jobs):
    cases = list(itertools.permutations(jobs, 3))
    result = []
    for case in cases:
        result.append(calculate_time(case))
    return min(result)

# 다른 사람의 풀이 
# 1) heap 구성   
# - 작업 소요를 기준으로 최소 heap을 만들어야한다.
# - 그러므로 [작업소요시간, 작업요청시점]의 형태로 heap을 구성해야한다.

# 2) 판별 
# - 현재 시점에 처리할 수 있는 작업인지 판단한다.
# - 조건) 이전 작업의 시작시간 < 현재 진행할 작업의 요청시점 <= 현재 시점 
# - 만약 현재 처리할 수 있는 작업이 없다면, 현재 시간 += 1 을 한다. 

import heapq

def solution2(jobs):
  answer, now, i = 0, 0, 0
  start = -1
  heap = []
  
  while i < len(jobs): 
    for job in jobs: # 현재시점에서 처리할 수 있는 작업을 heap에 저장 
      if start < job[0] <= now:
        heapq.heappush(heap, [job[1], job[0]])
        
    if len(heap) > 0: # heap에 처리할 작업이 있는 경우 
      curn = heapq.heappop(heap)
      start = now
      now += curn[0]
      answer += now - curn[1] # 작업 요청시간부터 종료시간까지의 시간계산 
      i += 1
    else: # 현재 처리할 작업이 없는 경우, 다음 시간으로 넘어감 
      now += 1
  return answer // len(jobs)

print(solution2(jobs))