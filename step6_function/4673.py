# 백준 단계별 풀이 6단계
# https://www.acmicpc.net/problem/4673

def d(n):
  for i in str(n):
    n += int(i)
  return n 

calculated_num = set()
for i in range(1, 10000):
  calculated_num.add(d(i))
result = set(range(1,10000)) - calculated_num
for data in sorted(result):
  print(data)


# def d(n):
#     x = 0
#     a = list(str(n))
#     for i in a:
#         x = x + int(i)
#     return n+x

# s_set = set()
# for k in range(1,10000):
#     s_set.add(d(k))
# ans = set(range(1,10000)) - s_set
# for num in sorted(ans):
#     print(num)
