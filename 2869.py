# 백준 단계별 풀이 8단계
# https://www.acmicpc.net/problem/2869

# 정상에 올라간 후에는 미끄러 지지 않는다. 
# 만약 낮에 정상에 올라갔으면 뺄셈이 없어야 한다. ==> 어떻게 구현? 

# up, down, height = map(int, input().split())
# result = 0
# count = 0 

# while True:
#   result += up
#   count += 1
#   if result >= height:
#     print(count)
#     break
#   else: 
#     result -= down 

# 반복문을 사용하면 시간초과가 발생한다. (시간제한 - 0.15초)

# 1) 생각해보면, 결국 어떻게든 낮에 정상에 도착할 수 밖에 없다. 
# 왜냐면 낮에는 덧셈이고 밤에는 뺄셈이니까, 덧셈의 결과값이 더 크지 뺄셈의 결과값이 더 클 수가 없다. 
# 하루에 올라가는 거리 = up - down 
# n일 후 낮에 정상에 도착하는 경우 ==> (up - down) * (n - 1) + up

# 2) 그럼 n은 어떻게 구하냐? 
# 밤에 정상에 도착하는 경우 ==> n = height / (up - down)
# 만약 낮에 정상에 도착한다고 하면, height가 down 만큼 낮으면 된다. 
# 그럼 마지막 날의 밤에 감소되는 만큼이 사라지는 거니까
# 즉, 뺄셈 한번이 감소되는 것이다.  
# 그러므로 n = (height - down) / (up - down)

# 3) n이 정수로 떨어지지 않으면? 
# 만약에 1.x 라던가, 이런 형태로 값이 떨어지면 올림을 하면 된다. 
# 즉, 1을 더해주자. 

up, down, height = map(int, input().split())
result = (height-down)/(up-down)
print(int(result) if result == int(result) else int(result) + 1)
