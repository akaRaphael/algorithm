# 백준 단계별 풀이 7단계
# https://www.acmicpc.net/problem/1157

# 아래 코드는 내가 푼 방식인데, 시간초과가 난다. 
# 2초를 넘어가는 것 같다.
# 시간복잡도는 O(N) 이라고 생각하는데, 이유를 잘 모르겠다. 왜그럴까?  

# n = input()
# n = n.lower()
# countNum = 0
# result = ''

# for data in n:
#   if countNum < n.count(data):
#     countNum = n.count(data)
#     prev = data 
#     result = data.upper()
#   elif countNum == n.count(data) and prev != data:
#     result = '?'

# print(result)

n_string = input().upper()
unique_string = list(set(n_string))
count_list = []

for data in unique_string:
  count = n_string.count(data)
  count_list.append(count)

if count_list.count(max(count_list)) > 1:
  print('?')
else:
  max_index = count_list.index(max(count_list))
  print(unique_string[max_index])
