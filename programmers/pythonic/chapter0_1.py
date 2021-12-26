test = [[1], [2]]
test2 = [[1,2], [3,4],[5]]

def solution(mylist): 
  answer = []
  for i in range(0, len(mylist)):
    answer.append(len(mylist[i]))
  return answer

print(solution(test2))