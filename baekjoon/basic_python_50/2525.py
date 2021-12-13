# 파이썬 50제 (1 ~ 50) - 오븐 시계
# https://www.acmicpc.net/problem/2525

hour, min = map(int, input().split())
wait = int(input())
sum_min = min + wait

if sum_min >= 60:
  hour += sum_min // 60
  min = sum_min - (sum_min // 60 * 60)

else:
  min = sum_min

if hour >= 24:
  hour = hour - 24

print(hour, min)