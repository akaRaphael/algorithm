# 백준 단계별 풀이 9단계 - 네 번째 점
# https://www.acmicpc.net/problem/3009

# 내가 생각한 풀이 
# 사각형의 4개의 좌표는 다음과 같은 조합을 이룬다
# min x, min y
# min x, max y
# max x, min y
# max x, max y
# 이 조합을 이용하면 max x와 min x, max y와 min y는 각각 2개씩을 갖는다. 
# 만약 1개씩 부족한 조합이 있다면, 비어있는 좌표가 정답이 된다.

x_list = []
y_list = []
for _ in range(3): 
  x, y = map(int, input().split())
  x_list.append(x)
  y_list.append(y)

for i in range(3):
  if x_list.count(x_list[i]) == 1:
    x = x_list[i]
  if y_list.count(y_list[i]) == 1:
    y = y_list[i]

print(x,y)