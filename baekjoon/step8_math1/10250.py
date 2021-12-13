# 백준 단계별 풀이 8단계
# https://www.acmicpc.net/problem/10250

# n번째 손님의 방의 거리(호수) = n / 높이
# n번째 손님의 방의 높이(층) = n % 높이

t = int(input())
for _ in range(t):
  height, room, guest = map(int, input().split())
  floor = guest % height * 100 if guest % height != 0 else height * 100
  distance = int(guest / height) if guest % height == 0 else int(guest/height) + 1
  guest_room = floor + distance 
  print(guest_room)


