# 프로그래머스 고득점 kit - stack/queue - 주식가격

# prices = 1초 단위로 기록된 주식가격 
# 입출력 예시
# input / return 
# [1, 2, 3, 2, 3]	/ [4, 3, 1, 1, 0]

prices = [1,2,3,2,3]

# 내가 작성한 코드 => 기본 문제는 통과했으나 효율성 문제에서 모두 실패함. 
def solution(prices):
  answer = []
  while len(prices) > 0:
    target = prices.pop(0)
    count = 0
    for i in range(len(prices)):
      if target <= prices[i]:
        count += 1
      else:
        count += 1
        break
    answer.append(count)
  return answer

print(solution(prices))
      

# 이중 for문을 이용한 방법 => 기본문제 + 효율성 모두 통과 
# 그러나 여전히 O(n^2)의 시간복잡도를 가지므로, input이 커지면 시간초과 발생
def solution1(prices):
  answer = [0] * len(prices)
  for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
      if prices[i] <= prices[j]:
        answer[i] += 1
      else:
        answer[i] += 1
        break
  return answer
  
# print(solution1(prices))

# Stack을 이용해서 푸는 방법 => O(n)
def solution2(prices):
  answer = [0] * len(prices)
  stack = []
  
  for i, price in enumerate(prices):
    while stack and price < prices[stack[-1]]:
      j = stack.pop()
      answer[j] = i - j
    stack.append(i)
    
  while stack:
    j = stack.pop()
    answer[j] = len(prices) - 1 - j
  
  return answer

# print(solution2(prices))
      