# 프로그래머스 고득점 kit - Greedy
# 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

# 입출력 예
# people / limit / return
# [70, 50, 80, 50] / 100 / 3
# [70, 80, 50] / 100 / 3

people = [70, 50, 60, 80, 50, 40, 40, 40, 40] 
limit = 100
# 내가 짠 코드 
# 최소 무게가 40키로라는 점을 이용한다.
# 한 사람을 태우고 남은 무게가 40보다 작으면 패스 
# 남은 무게가 40보다 크다면 남은 거에서 순회해서 남은무게보다 작거나 같은 무게를 가진 사람을 찾음

def solution(people, limit):
  
  # 최소 힙 사용해서 풀어보자 
  count = 0
  stack = list()
  people = sorted(people, reverse=True)
  idx = 0 
  while idx < len(people):
    if limit - people[idx] < 40:
      people.pop(idx)
      count += 1
    else:
      break
      
  mock = sum(people) // limit
  count += mock
  if sum(people) % limit:
    count += 1
  
  return count

print(solution(people, limit))
      
      
  