# for 문과 if문을 한번에
# https://programmers.co.kr/learn/courses/4008/lessons/48463

mylist = [3,2,6,7]

def solution(mylist):
  answer = [data ** 2 for data in mylist if data % 2 == 0]
  return answer

print(solution(mylist))