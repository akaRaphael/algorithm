# 11653 - 내가 적은 코드는 2초, 이 코드는 90ms 걸림 
# 0.5를 곱하는건 어디서 온 걸까? 신기하다. 찾아보자.
import sys

N = int(sys.stdin.readline().rstrip())
for i in range(2, int(N ** 0.5) + 1):
    while N % i == 0:
        print(i)
        N //= i
if N > 1:
    print(N)

#==========================================================================
# 2581 - 나는 1000ms 걸렸는데 이 코드는 76ms 걸림 
# 메소드를 정의해서 이용하면 훨씬 빠르다! 라는 것을 알게 되었다! 
def point(n) :
    solve = [True] * (n + 1)
    solve[1] = False
    m = n**0.5
    for i in range(2, int(m) +1) :
        if solve[i] == True :
            for j in range( i*i, n + 1, i) :
                solve[j] = False
    return solve

N = int(input())
M = int(input())

solve = point(M)
ans = []
for i in range(N, M+1) :
    if solve[i] == True:
        ans.append(i)

if len(ans) > 0 :
    print(sum(ans), ans[0])
else :
    print(-1)

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

#==========================================================================
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