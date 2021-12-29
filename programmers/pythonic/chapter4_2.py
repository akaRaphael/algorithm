# i번째 원소와 i+1번째 원소
# https://programmers.co.kr/learn/courses/4008/lessons/72546

# 입출력 예시
# mylist / output
# [83, 48, 13, 4, 71, 11]	/ [35, 35, 9, 67, 60]

mylist = [83, 48, 13, 4, 71, 11]

# 내가 짠 코드 
def solution(mylist):
  answer = []
  for idx in range(len(mylist) - 1):
    answer.append(abs(mylist[idx] - mylist[idx + 1]))
  return answer

print(solution(mylist))

# pythonic한 코드 
# zip의 특성을 이용한 코드
# 길이가 다른 iterable 2개가 주어졌을 때, 길이가 짧은 iterable만큼만 짝을 만들고 나머지는 버린다.
# 문제에서 마지막 요소는 다음 원소가 없기 때문에 차이를 구할 수 없다는 조건으로 인해 가능한 방법.
def solution2(mylist):
  answer = []
  for number1, number2 in zip(mylist, mylist[1:]):
    answer.append(abs(number1 - number2))
  return answer

print(solution2(mylist)) 