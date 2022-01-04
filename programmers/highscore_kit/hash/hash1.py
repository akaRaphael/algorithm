# 프로그래머스 고득점 kit - hash
# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

import collections

# 내가 짠 코드 ==> 통과 
participants = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "mislav", "ana"]
def solution(participants, completion):
  result = collections.defaultdict(int)
  for name in participants:
    result[name] += 1
    
  for name in completion:
    if result[name]:
      result[name] -= 1
      
  result = sorted(result.items(), key = lambda x: x[1])
  answer = result[-1][0]
  return answer

print(solution(participants, completion))

# 프로그래머스에서 좋아요가 가장 많은 솔루션 
def solution2(participants, completion):
  answer = collections.Counter(participants) - collections.Counter(completion)
  return list(answer.keys())[0]

print(solution2(participants, completion))

# Hash를 이용한 솔루션 
def solution3(participants, completion):
  hash_dict = {}
  sum_hash = 0
  
  for part in participants:
    hash_dict[hash(part)] = part
    sum_hash += hash(part)
    
  for comp in completion:
    sum_hash -= hash(comp)
    
  # 남은 hash 값이 완주하지 못한 선수 
  return hash_dict[sum_hash]

print(solution3(participants, completion))