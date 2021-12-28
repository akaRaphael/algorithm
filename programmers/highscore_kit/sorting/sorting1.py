# 프로그래머스 고득점 kit - 정렬part
# k 번째 수 찾기 - https://programmers.co.kr/learn/courses/30/lessons/42748

# 입출력 예
# array	 / commands	/ return
# [1, 5, 2, 6, 3, 7, 4]	/ [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	/ [5, 6, 3]

array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
  answer = []
  for i, j, k in commands:
    answer.append(sorted(array[i - 1 : j])[k - 1])
  return answer

print(solution(array, commands))

# 가장 좋아요를 많이 받은 솔루션 

def solution2(array, commands):
  return list(map(lambda x: sorted(array[x[0]-1 : x[1]])[x[2]-1], commands))

print(solution2(array, commands))