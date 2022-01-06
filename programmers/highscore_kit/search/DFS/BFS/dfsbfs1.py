# 프로그래머스 고득점kit - DFS/BFS
# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

numbers = [1,1,1,1,1]
target = 3

# 와 이건 진짜 모르겠다... 재귀적 사고를 좀 더 공부해야겠다.
# 고득점 kit 복습 및 정리할 때 다시 꼭 풀어볼 것 

# 다른 사람의 솔루션 - DFS 풀이 1
def dfs1(array, numbers, target, size):
  answer = 0
  if len(array) == size:
    if sum(array) == target:
      return 1
    else:
      return 0
  else:
    A = numbers.pop(0)
    for i in [1, -1]:
      array.append(A * i)
      answer += dfs1(array, numbers, target, size)
      array.pop()
    numbers.append(A)
    return answer
  
  
def solution1(numbers, target):
  answer = 0
  answer += dfs1([numbers[0]], numbers[1:], target, len(numbers))
  answer += dfs1([-numbers[0]], numbers[1:], target, len(numbers))
  return answer

solution1(numbers, target)

# 다른 사람의 풀이 - DFS 풀이 2
answer = 0
def DFS2(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS2(idx+1,numbers,target,value+numbers[idx])
    DFS2(idx+1,numbers,target,value-numbers[idx])

def solution2(numbers, target):
    global answer
    DFS2(0,numbers,target,0)
    return answer


# 다른 사람의 풀이 - BFS 풀이 
import collections
def solution3(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])
    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum+number, num_idx + 1))
            stack.append((current_sum-number, num_idx + 1))

    return answer

# 다른 사람의 풀이 - 완전탐색 풀이 
from itertools import product
def solution4(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
  
  
# 프로그래머스에서 좋아요가 가장 많은 풀이 
def solution5(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution5(numbers[1:], target-numbers[0]) + solution5(numbers[1:], target+numbers[0])