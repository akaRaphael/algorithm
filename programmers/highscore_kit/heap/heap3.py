# 프로그래머스 고득점 kit - heap
# 이중우선순위큐
# https://programmers.co.kr/learn/courses/30/lessons/42628

# 입출력 예시 
# input / return 
# ["I 16","D 1"] / [0, 0]
# ["I 7","I 5","I -5","D -1"] / [7, 5]

operations = ["I 7","I 5","I -5","D -1"] 

# 내가 짠 코드 => 통과 
# - 그러나 문제의 출제 의도에 맞는 솔루션은 아님 
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


# 다른사람이 작성한 코드 
import heapq
def solution2(arguments):
  max_heap = []
  min_heap = []
  for arg in arguments:
    if arg == "D 1":
      if max_heap != []:
          heapq.heappop(max_heap)
          if max_heap == [] or -max_heap[0] < min_heap[0]:
              min_heap = []
              max_heap = []
    elif arg == "D -1":
      if min_heap != []:
          heapq.heappop(min_heap)
          if min_heap == [] or -max_heap[0] < min_heap[0]:
              max_heap = []
              min_heap = []
    else:
      num = int(arg[2:])
      heapq.heappush(max_heap, -num)
      heapq.heappush(min_heap, num)
  if min_heap == []:
      return [0, 0]
  return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]

print(solution2(operations))