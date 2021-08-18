t = int(input())
for _ in range(t):
  univ = []
  alcho = []
  t2 = int(input())
  for _ in range(t2):
    a, b = input().split()
    univ.append(a)
    alcho.append(int(b))
  print(univ[alcho.index(max(alcho))])
