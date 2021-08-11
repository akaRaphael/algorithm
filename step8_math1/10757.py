# 백준 단계별 풀이 8단계
# https://www.acmicpc.net/problem/10757

a, b = map(int, input().split())
print(a + b) 

# C언어의 경우, 자료형에 따른 메모리가 한정되어 있기 때문에
# 10757번 같은 문제를 풀기 어렵다. 
# 파이썬의 경우, 언어 자체적으로 BigInt를 지원하기 때문에 문제없이 연산이 가능하다. 
# 그렇다면 파이썬이 Integer로 표현할 수 있는 최대값은 몇일까?

import sys
max_num = sys.maxsize
max_num2 = sys.maxsize + 1

print("max_num =", type(max_num), max_num) # <class 'int'> 9223372036854775807 <== 900경
print("max_num2 =", type(max_num), max_num2) # <class 'int'> 9223372036854775808 <== 900경
