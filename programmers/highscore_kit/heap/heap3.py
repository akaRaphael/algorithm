# 프로그래머스 고득점 kit - heap
# 이중우선순위큐
# https://programmers.co.kr/learn/courses/30/lessons/42628

# 입출력 예시 
# input / return 
# ["I 16","D 1"] / [0, 0]
# ["I 7","I 5","I -5","D -1"] / [7, 5]

operations = ["I 7","I 5","I -5","D -1"] 

# 내가 짠 코드 => 통과 
def solution(operations):
  answer = []
  for command in operations:
    operator, operand = command.split(' ')
    if operator == "I":
      answer.append(int(operand))
    elif operator == "D" and answer != []:
      if operand.find("-") != -1:
        answer.remove(min(answer))
      else:
        answer.remove(max(answer))
  if answer == []:
    return [0,0]    
  
  return [max(answer), min(answer)]

print(solution(operations))