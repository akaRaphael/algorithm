# 백준 단계별 풀이 9단계 - 골드바흐의 추측
# https://www.acmicpc.net/problem/9020

# def prime(n): #에라토스테네스의 체 
#   a = [True] * n
#   sqrt = int(n ** 0.5)
#   for i in range(2, sqrt + 1):
#     if a[i]:
#       for j in range(i + i, n, i):
#         a[j] = False
#   return [i for i in range(2, n) if a[i] == True]

# def sosu(n):
#   p_list = prime(n)
#   idx = max([i for i in range(len(p_list)) if p_list[i] <= n / 2]) # 가장 큰 수의 index
#   for i in range(idx, -1, -1): # 큰 수 부터 작은 수
#     for j in range(i, len(p_list)): # 작은 수 부터 큰 수 
#       if p_list[i] + p_list[j] == n:
#         return [p_list[i], p_list[j]]

# for _ in range(int(input())):
#   n = int(input())
#   print(" ".join(map(str, sosu(n)))) # 리스트를 한줄 출력 하는 방법

  ############################################## 개선된 코드 
import sys
input = sys.stdin.readline

def isPrime(x) :
    if x < 2 :
        return False
    for i in range(2, int(x**0.5)+1) :
        if x % i == 0 :
            return False
    
    return True

for _ in range(int(input())) :
    n = int(input())
    
    for i in range(n//2, -1, -1) :
        if isPrime(i) and isPrime(n-i) :
            print(i, n-i)
            break