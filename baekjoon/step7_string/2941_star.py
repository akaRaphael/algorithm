# 백준 단계별 풀이 7단계
# https://www.acmicpc.net/problem/2941

input_s = input()
croatic_char = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=","z="]

for data in croatic_char:
  input_s = input_s.replace(data, '*')

print(len(input_s))