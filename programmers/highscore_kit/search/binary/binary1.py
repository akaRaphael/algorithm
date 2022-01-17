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
  left = 1 
  right = max(times) * n # 가장 비효율적으로 심사를 받는 경우 
  while left <= right:
    mid = (left + right) // 2
    people = 0
    for time in times:
      people += mid // time
      if people >= n:
        break
    
    if people >= n:
      answer = mid
      right = mid - 1
    elif people < n:
      left = mid + 1
  
  return answer
      
print(solution(n, times))