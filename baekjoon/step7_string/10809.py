# 백준 단계별 풀이 7단계
# https://www.acmicpc.net/problem/10809

import string
s_input = input()
for char in string.ascii_lowercase:
  print(s_input.find(char), end=" ")

# string.find(chr) ==> chr이 문자열의 몇번 index에 있는지 반환. 없으면 -1 반환 