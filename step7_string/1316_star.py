# 백준 단계별 풀이 7단계
# https://www.acmicpc.net/problem/1316

n = int(input())
count = 0

for _ in range(n):
  word = input()
  error = 0
  for index in range(len(word) - 1):
    if word[index] != word[index + 1]:
      new_word = word[index + 1:]
      if new_word.count(word[index]) > 0:
        error += 1
  if error == 0:
    count += 1

print(count)