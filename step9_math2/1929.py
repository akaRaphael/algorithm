# 백준 단계별 풀이 9단계
# https://www.acmicpc.net/problem/1929

# def check_yaksoo(n):
#   if n == 1:
#     return False
#   else:
#     for i in range(2, int(n ** 0.5) + 1):
#       if n % i == 0:
#         return False
#     return True

# m, n = map(int, input().split())
# for i in range(m, n + 1):
#   if check_yaksoo(i):
#     print(i)

# 에라토스테네스의 체를 이용한 방식
import sys
input = sys.stdin.readline


#n 이하의 체를 구하는 함수
def prime(n):
  #0과1은 소수가아니므로 False, 나머지 2부터 n까지는 n-1개임
	seive = [False, False] + [ True ] * (n-1)
	k = int(n ** 0.5)

	#2~ 루트n + 1까지
	for i in range(2, k+1):
		if seive[i]:
			for j in range(i+i, n+1, i):
				seive[j] = False
	return [ i for i in range(2, n+1) if seive[i] == True]

m, n = map(int, input().split())
prime_list = prime(n)
for i in prime_list:
	if i < m:
		continue
	print(i)
