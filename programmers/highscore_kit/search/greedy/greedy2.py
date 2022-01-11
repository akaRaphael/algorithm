# 프로그래머스 고득점 kit - Greedy
# 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860

# ***** 내가 풀지 못한 문제 => 테스트케이스 10번 11번이 계속 틀림 

name = "JAAAZZ"

# 다른사람의 솔루션 
def solution(name):
  change = [min(ord(i) - 65, 90 - ord(i) + 1) for i in name]
  idx = 0
  answer = 0
  
  while True:
    answer += change[idx]
    change[idx] = 0
    if sum(change) == 0:
      return answer
    
    left, right = 1, 1
    while change[idx - left] == 0:
      left += 1
    while change[idx + right] == 0:
      right += 1
      
    answer += left if left < right else right
    idx += -left if left < right else right
    
print(solution(name))


      
    