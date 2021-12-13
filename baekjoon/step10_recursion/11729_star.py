# 백준 단계별 풀이 10단계 - 하노이의 탑
# https://www.acmicpc.net/problem/11729
n = int(input())
def hanoi(n, start, other, to): #start(시작기둥), to(목표기둥), other(남은기둥)
    if n == 1:
        print(start, to)
    else:
        hanoi(n - 1, start, to, other)
        print(start, to)
        hanoi(n - 1, other, start, to)
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)