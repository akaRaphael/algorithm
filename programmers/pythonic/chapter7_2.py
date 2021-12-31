# flag OR for-else
# https://programmers.co.kr/learn/courses/4008/lessons/66568

# 내가 짠 코드 
import math
a = [int(input()) for _ in range(5)]
result = 1
flag = False

for number in a:
  result *= number
  if math.sqrt(result) == int(math.sqrt(result)):
    flag = True

if flag:
  print("found")
else:
  print("not found")

# pythonic한 코드 - flag 변수를 사용하지 않고 for-else를 사용

numbers = [int(input()) for _ in range(5)]
result = 1

for number in numbers:
  result *= number
  if math.sqrt(result) == int(math.sqrt(result)):
    print("found")
    break
else:
  print("not found")