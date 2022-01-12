# 프로그래머스 고득점 kit - Greedy
# 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

# 입출력 예
# people / limit / return
# [70, 50, 80, 50] / 100 / 3
# [70, 80, 50] / 100 / 3


# *********** 스스로 풀지 못한 문제 (4시간 투자함)

people = [70, 80, 50] 
limit = 100

# 다른 사람의 솔루션 
def solution(people, limit):
  left = 0
  right = len(people) - 1
  count = 0
  people.sort()
  
  while left <= right:
    count += 1
    if people[left] + people[right] <= limit:
      left += 1
    right -= 1
      
  return count

print(solution(people, limit))

# *이 문제의 포인트
# 가장 무거운 사람을 태우되 남은 1자리를 가벼운 사람부터 차례대로 고려한다. 
# 남은 사람들 중 가장 가벼운데 무게가 초과됬다는 말은 두번째로 가벼운 사람 역시 초과될 것이라는 뜻. 
# 더 이상 고려할 필요가 없게 된다. 
# 초과되면 무거운 사람만 보트에 한명 태우고 나머지 형식도 
# 반복해서 최대한 무거운+가벼운 사람의 조합을 사용해 보트를 최소화 한다.