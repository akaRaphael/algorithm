# 백준 단계별 풀이 6단계
# https://www.acmicpc.net/problem/1065

n = int(input())
hansu = 0 

for n in range(1, n + 1):
  if n < 100:
    hansu += 1
  else:
    n_list = list(map(int, str(n)))
    if n_list[0] - n_list[1] == n_list[1] - n_list[2]:
      hansu += 1

print(hansu)


# 개선된 코드
n = int(input())
hansu = 99 # 99까지는 모두 등차수열이다. 

if n < 100:
  print(n)
else:
  for i in range(100, n + 1):
    n_list = list(map(int, str(i)))
    if n_list[0] - n_list[1] == n_list[1] - n_list[2]:
      hansu += 1
  print(hansu)  