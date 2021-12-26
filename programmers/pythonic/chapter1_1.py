test = [[1], [2]]
test2 = [[1,2], [3,4],[5]]

# 내가 짠 코드 
def solution(mylist): 
  answer = []
  for i in range(len(mylist)):
    answer.append(len(mylist[i]))
  return answer

print(solution(test2))

# pythonic 하게 짠 코드 
def solution2(mylist):
  return list(map(len, mylist))

print(solution2(test2))