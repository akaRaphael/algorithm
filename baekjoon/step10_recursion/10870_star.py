# 백준 단계별 풀이 10단계 - 피보나치 5
# https://www.acmicpc.net/problem/10870

def fibonacci(n):
  if n <= 1:
    return n 
  return fibonacci(n-1) + fibonacci(n - 2)

n = int(input())
print(fibonacci(n))

# 재귀함수는 역시 연습을 많이 해야겠다. 
# 더불어 재귀 + 피보나치 수열은 헷갈린다. 