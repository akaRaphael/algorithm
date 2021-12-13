# 백준 단계별 풀이 2단계 
# https://www.acmicpc.net/problem/2753

year = int(input())
if(year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
    print(1)
else:
    print(0)