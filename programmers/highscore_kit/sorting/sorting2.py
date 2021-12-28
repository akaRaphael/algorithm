# 프로그래머스 고득점 kit - 정렬
# 가장 큰 수 - https://programmers.co.kr/learn/courses/30/lessons/42746

# 1. 순서가 어떻게 조합되든 동일한 자릿수의 수가 만들어진다.
# 2. 각 요소의 가장 큰 자릿수를 추출한다.
# ex) 10이면 1, 6이면 6, 200이면 2 
# 3. 자릿수가 큰 순서대로 조합한다.
# => 여기서 문제점이 생긴다. 30과 3이 있다면 303이나온다. 
#    그러나, 330이 최대값이다. 어떻게 해결할까?  

# 입출력 예
# numbers	/ return
# [6, 10, 2]	/ "6210"
# [3, 30, 34, 5, 9]	/ "9534330"

numbers = [3, 30, 34, 5, 9]	

# 내가 짠 코드 
# => 위에서 말했던 문제점이 발생했다.
#    30과 3이 있다면 303이나온다. 그러나, 330이 최대값이다.
#    어떻게 해결해야 할지 모르겠다.   
def solution(numbers):
  candidate = {}
  answer = ""
  numbers = sorted(numbers, reverse=True)
  
  for idx, num in enumerate(numbers):
    num = str(num)
    candidate[idx] = num[0]
    
  candidate = sorted(candidate.items(), key = lambda x:x[1], reverse=True)
  for idx, num in candidate:
    answer+= str(numbers[idx])
  return answer

# 검색으로 찾은 solution
# - 아래 코드의 핵심은 lambda 식에 있다.
# - 문자열을 3번 반복하여 문자로된 숫자를 최소 1000단위로 만든다. ex) 3 => 333
#   여기에는 두가지 이유가 있다. 

#   1) 문제의 제한사항에 원소의 값이 최대 1000 이기 때문이다.
#   2) 문자열 비교의 특성상 0번째 문자가 같은 경우 1번째 문자를 비교하고, 
#      1번째 문자도 같은 경우에는 길이가 짧은 문자열이 앞쪽에 배치되기 때문이다.
#   ex) 3과 30의 경우, 333과 303030을 비교하게 된다. 
#       index 0번의 문자는 3으로 동일하다. 
#       index 1번의 문자는 3과 0으로, 333이 우선순위를 갖게 된다. 

# - 마지막으로 return 문에서 문자열을 int로 변환하고, 다시 str로 변환한다.
#   이는 조합된 numbers에 들어있는 문자가 [0,0,0,0]인 경우를 대비하기 위해서다.
#   [0,0,0,0]을 join으로 붙여버리면, 0000이 된다. 그러나 이것은 문제가 원하는 답이 아니다.
#   문제가 원하는 것은 가장 큰 수를 이루는 조합을 찾는 것이기 때문이다. 0000은 그냥 0이다. 
#   그러므로 0000을 int로 변환하여 0으로 만들어 준 뒤, 이를 다시 문자로 변환하여 출력한다. 

def solution2(numbers):
  numbers = list(map(str, numbers))
  numbers.sort(key = lambda x: x * 3, reverse = True)
  return str(int("".join(numbers)))

print(solution2(numbers))