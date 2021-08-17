# 백준 단계별 풀이 10단계 - 별 찍기 - 10
# https://www.acmicpc.net/problem/2447

# 나는 컴공을 전공하지는 않았지만 컴퓨터 관련 학과를 전공한 사람으로서,
# C언어 수업을 들었을 때부터 별찍기를 진짜 못했다. 
# 별 찍기는 너무 어렵다. 

# 풀이방법
# n을 입력 받아서 n * n 형태의 정사각형으로 별을 찍는다. 
# n > 3인 경우 n/3 * n/3 형태의 정사각형으로 별을 찍는다. 
# n이 3의 배수인 경우, 문제에서 말하는 형태의 별을 찍는다. 

def draw_star(n) :
    global Map
    
    if n == 3 :
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return

    a = n // 3
    draw_star(n // 3)
    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 :
                continue
            for k in range(a) :
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어

N = int(input())      
Map = [[0 for i in range(N)] for i in range(N)]
draw_star(N)

for i in Map :
    for j in i :
        if j :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()

# 출처 - https://study-all-night.tistory.com/5