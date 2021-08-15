t = int(input())
for _ in range(t):
  a, b = map(int, input().split())
  if a == 1:
    print(b)
    break
  elif b == 1:
    print(a)
    break
  else:
    start = b // a
    a_list = 
