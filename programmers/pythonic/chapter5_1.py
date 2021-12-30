# sequence 멤버를 하나로 이어붙이기
# https://programmers.co.kr/learn/courses/4008/lessons/13354

mylist = ['1', '100', '33']

def solution(mylist):
  answer = "".join(mylist)
  return answer

print(solution(mylist))