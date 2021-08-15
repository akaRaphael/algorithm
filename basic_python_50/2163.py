# 파이썬 50제 (1 ~ 50) - 초콜릿 쪼개기  
# https://www.acmicpc.net/problem/2163

# n * m 초콜릿을 1 * 1로 쪼개는 규칙은 n * m -1 이다. 
n, m = map(int, input().split())
print(n * m -1)