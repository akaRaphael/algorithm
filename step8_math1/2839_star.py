# 백준 단계별 풀이 8단계
# https://www.acmicpc.net/problem/2839

#################### 내가 작성한 코드 ==> 틀림 ==> 예외처리 부족인 것 같다. 
# n = int(input())
# bag_count = 0

# if n % 5 == 0:
#   bag_count += n // 5
#   print("first bag_count =", bag_count)
# elif (n % 5) % 3 == 0:
#   bag_count += n // 5
#   n = n % 5
#   bag_count += n // 3
#   n = n % 3
#   if n == 0:
#     print("second bag_count =", bag_count)
#   else:
#     print("second exception = ", n)
# elif n % 3 == 0:
#   bag_count += n // 3
#   print("third bag_count =", bag_count)
# elif n >= 5:
#   n = n - 5
#   bag_count += 1
#   if n % 3 == 0:
#     bag_count += n // 3
#     print("fourth bag_count =", bag_count) 
#   else:
#     print("third exception = ", n)
# else:
#   print(-1)

# 최소 봉지 개수의 조합을 짜려면 우선 5단위로 끊어야 한다. 
# 5단위로 끊고 남은 나머지에 따라 조건문이 달라진다. 
# 5로 나누기 떄문에 1 ~ 4 까지의 나머지가 생길 수 있다. 

# case 0) 나머지가 없는 경우, 5로 나눈 몫을 그대로 가져간다. 
# case 1) 나머지가 1인 경우, 5로 나눈 몫을 1개(5) 줄이고 나머지 1 + 5를 3단위로 나눈다.  
# case 2) 나머지가 2인 경우, 5로 나눈 몫을 2개(10) 줄이고 나머지 2 + 10을 3단위로 나눈다.  
# case 3) 나머지가 3인 경우, 5로 나눈 몫은 그대로 가져가고, 나머지 3을 3단위로 나눈다.  
# case 4) 나머지가 4인 경우, 5로 나눈 몫을 1개(5) 줄이고 나머지 4 + 5를 3단위로 나눈다 
# case 5) 5로 나눈 몫이 0인데 3 미만의 나머지가 있는 경우, -1을 출력한다. 

n = int(input())
bag_five = 0
bag_three = 0

if n % 5 == 0:
  bag_five = n // 5
  print(bag_five + bag_three)
elif (n // 5 >= 1) and (n % 5 == 1):
  bag_five = n // 5 - 1
  n = n - bag_five * 5
  bag_three = n // 3
  print(bag_five + bag_three)
elif (n // 5 >= 2) and (n % 5 == 2):
  bag_five = n // 5 - 2
  n = n - bag_five * 5
  bag_three = n // 3
  print(bag_five + bag_three)
elif n % 5 == 3:
  bag_five = n // 5
  n = n - bag_five * 5
  bag_three = n // 3
  print(bag_five + bag_three)
elif (n // 5 >= 1) and (n % 5 == 4):
  bag_five = n // 5 - 1
  n = n - bag_five * 5
  bag_three = n // 3
  print(bag_five + bag_three)
else:
  print(-1)



