# 프로그래머스 고득점 kit - DP
# N으로 표현
# https://programmers.co.kr/learn/courses/30/lessons/42895

# 입출력 예
# N	/ number /	return
# 5	/ 12 / 4
# 2	/ 11 / 3

# 다른사람의 풀이
# https://www.youtube.com/watch?v=ZsVVTEfZee8

N = 5
number = 12

# DP = 큰 문제를 여러개의 작은 문제로 쪼개어 접근 
def solution(N, number):
  if number == N:
    return 1
  
  answer = -1 
  li = [set() for i in range(8)]
  # li = [set()] * 8 이렇게 만들면 8개의 set이 모두 동일한 메모리 주소값을 갖는다. 
  # 그러므로 첫번째 set에 하나의 원소가 추가되면 나머지 7개 원소에도 동일하게 추가된다. 

  # set을 이용하는 방법 
  # 1  2  3    4    5  => N번째 set을 의미 
  # 5 55 555 5555 55555  

  for i in range(len(li)):
    li[i].add(int(str(N) * (i + 1)))
    
  for i in range(1, 8):
    for j in range(i):
      for op1 in li[j]:
        for op2 in li[i - j - 1]:
          li[i].add(op1 - op2)
          li[i].add(op1 + op2)
          li[i].add(op1 * op2)
          if op2 != 0:
              li[i].add(op1 // op2)
              
    if number in li[i]:
      answer = i + 1
      break
    
  return answer
  
print(solution(N, number))
  
# 프로그래머스 최다 좋아요 솔루션 
def solution2(N, number):
  S = [{N}]
  for i in range(2, 9):
      lst = [int(str(N)*i)]
      for X_i in range(0, int(i / 2)):
          for x in S[X_i]:
              for y in S[i - X_i - 2]:
                  lst.append(x + y)
                  lst.append(x - y)
                  lst.append(y - x)
                  lst.append(x * y)
                  if x != 0: lst.append(y // x)
                  if y != 0: lst.append(x // y)
      if number in set(lst):
          return i
      S.append(lst)
  return -1
