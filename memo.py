# 2839번 - 짧은 코드 
N = int(input())

bag = 0
while N >= 0:
    if N % 5 == 0:  # 5의 배수이면
        bag += (N // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    N -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else:
    print(-1)

# 1101번 76ms 짜리 코드 
from sys import stdin
import math

T = int(stdin.readline())

for _ in range(T):
    x, y = map(int, stdin.readline().split())
    distance = y - x

    if distance <= 3:
        print(distance)
        
    else:
        n = int(math.sqrt(distance))
        print(n)
        if distance == n ** 2:
            print(2*n-1)
        elif n ** 2 < distance <= n ** 2 + n:
            print(2*n)
        else:
            print(2*n+1)