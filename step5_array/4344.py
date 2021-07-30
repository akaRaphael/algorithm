# 백준 단계별 풀이 5단계
# https://www.acmicpc.net/problem/4344

import sys

caseNum = int(input())
for _ in range(caseNum):
  arr = list(map(int, sys.stdin.readline().split()))
  average = sum(arr[1:]) / arr[0]
  count = 0
  for score in arr[1:]:
    if score > average:
      count += 1
  result = count / arr[0] * 100
  print(f'{result:.3f}%')

  # 중간에 평균 넘는 사람 구하는 부분을 이렇게 작성했는데 
  # 백준에서는 틀렸다고 나오더라... 
  # 아마 아래의 for문을 쓰면 안되는거 같음 
  # aboveAvg = [data for data in arr if data > average]
  # result = round(len(aboveAvg)/arr[0]*100,3)
  # print(f'{result:.3f}%')
