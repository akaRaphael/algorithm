# 파이썬 50제 (1 ~ 50) - 최소공배수
# https://www.acmicpc.net/problem/1934

# greatest common divisor of integer a and b
def gcd(a, b):
    return gcd(b, a % b) if b else a

# least common multiple of integer a and b 
def lcm(a, b):
    return a * b // gcd(a, b)

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))
