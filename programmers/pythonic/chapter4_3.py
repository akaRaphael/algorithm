# 모든 멤버의 type 변환하기
# https://programmers.co.kr/learn/courses/4008/lessons/13328

def solution(mylist):
  answer = list(map(int, mylist))
  return answer

print(solution(['1', '100', '33']))