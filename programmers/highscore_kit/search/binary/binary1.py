# 프로그래머스 고득점 kit - 이분탐색 
# 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238

# 입출력 예
# n	/ times	/ return
# 6	/ [7, 10] /	28

n = 6
times = [7, 10]

# 다른 사람의 풀이 
def solution(n, times):
  answer = 0
  left = 1 # 최소값 
  right = max(times) * n # 가장 비효율적으로 심사를 받는 경우 
  while left <= right: # 이진탐색 
    mid = (left + right) // 2 # 중간 값 
    people = 0
    for time in times: 
      people += mid // time # mid분 동안 모든 심사관이 심사한 사람의 수 
      if people >= n:
        break
    
    if people >= n: # 심사한 사람의 수가 n과 같거나 많은 경우 
      answer = mid
      right = mid - 1
    else: # 심사한 사람의 수가 n보다 적은 경우 
      left = mid + 1
  
  return answer
      
print(solution(n, times))