# 백준 단계별 풀이 2단계 
# https://www.acmicpc.net/problem/1330

a, b = map(int, input().split())

if(a < b):
    print("<")
elif (a > b):
    print(">")
elif (a == b):
    print("==")