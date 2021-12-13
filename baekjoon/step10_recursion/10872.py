# 백준 단계별 풀이 10단계 - 팩토리얼 
# https://www.acmicpc.net/problem/10872

# 내가 작성한 코드 
# 무엇인가 재귀적이다 라는 느낌이 없다
# 재귀적이기 보다는 콜백의 느낌이 가까운 것 같다. 

# def factorial(n):
#   result = 1
#   while n > 0:
#     result *= n
#     n -= 1
#     factorial(n)
#   return result

# n = int(input())
# print(factorial(n))

################### 개선된 코드

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))
