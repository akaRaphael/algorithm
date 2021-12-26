# n진법으로 표기된 string을 10진법 숫자로 변환하기
# https://programmers.co.kr/learn/courses/4008/lessons/13168

num, base = map(int, input().strip().split(' '))
answer = 0
num = str(num)

for idx, number in enumerate(num[::-1]):
  answer += int(number) * (base ** idx)

print(answer)


# pythonic한 코드 
print(int(num, base))