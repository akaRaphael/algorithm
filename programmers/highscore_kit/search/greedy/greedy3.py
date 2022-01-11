# 프로그래머스 고득점 kit - Greedy
# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

# 문자열의 순서를 지킨 상태에서 가장 큰 수를 만드는 조합을 찾아야 한다. 


# ********** 내가 풀지 못한 문제 

# 다른 사람의 솔루션 
number = "4177252841"
k = 4

def solution(number, k):
  number = list(number)
  stack = list()
  
  for num in number:
    while stack and stack[-1] < num and k > 0:
      stack.pop()
      k -= 1
    else:
      stack.append(num)

  if k > 0:
    stack = stack[:len(stack) - k]
  
  return "".join(stack)

print(solution(number, k))