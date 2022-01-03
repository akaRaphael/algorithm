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

# 프로그래머스 좋아요 1등 
def solution2(participants, completion):
  answer = collections.Counter(participants) - collections.Counter(completion)
  return list(answer.keys())[0]

print(solution2(participants, completion))
