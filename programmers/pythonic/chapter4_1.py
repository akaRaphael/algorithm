# 2차원 리스트 뒤집기
# https://programmers.co.kr/learn/courses/4008/lessons/13339

mylist = [[1,2,3], [4,5,6], [7,8,9]]

# 내가 작성한 코드 
def solution(mylist):
  answer  = []
  temp = []
  for i in range(len(mylist)):
    for j in range(len(mylist)):
      temp.append(mylist[j][i])
    answer.append(temp)
    temp = []
  return answer


# pythonic한 코드 - zip 사용
# zip은 2개 이상의 iterable을 매개변수로 받는다.(매개변수가 1개라도 에러는 발생하지 않는다.)
# 각 iterable의 동일한 index 번호에 위치한 값을 튜플로 묶어준다. 
# 매개변수로 들어가는 각 iterable은 동일한 길이를 가져야 한다.
# 각 iterable의 길이가 다른 경우, 쌍을 이룰 수 있는 요소만큼 튜플로 묶고 나머지는 버려진다.
def solution2(mylist):
  new_list = list(map(list, zip(*mylist)))
  return new_list

print(solution2(mylist))