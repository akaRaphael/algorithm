# 백준 단계별 풀이 8단계
# https://www.acmicpc.net/problem/1712

fc, pc, sp = map(int, input().split())
if pc >= sp:
  print(-1)
else: print(int(fc/(sp-pc) + 1))