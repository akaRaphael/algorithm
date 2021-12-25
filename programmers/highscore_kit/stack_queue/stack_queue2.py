# 프로그래머스 고득점 kit - stack/queue - 프린터 

# 입출력 예시
# priorities / location / return
# [2, 1, 3, 2] / 2 / 1
# [1, 1, 9, 1, 1, 1] / 0 / 5

# 내가 생각한 풀이 - 2일 고민하고 해결 (12월 24일 ~ 12월 25일)
def solution(priorities, location):
  answer = 0
  count = 0 
  while len(priorities) != 0:
    max_num = max(priorities)
    if priorities[0] < max_num:
      temp = priorities.pop(0)
      priorities.append(temp)
      if location > 0:
        location -= 1
      else:
        location = len(priorities) - 1
    elif priorities[0] == max_num:
      if location != 0:
        priorities.pop(0)
        location -= 1
        count += 1
      else:
        answer = count + 1
        break
  return answer


# 프로그래머스에서 가장 좋아요를 많이 받은 솔루션
def solution2(priorities, location):
  queue =  [(i,p) for i,p in enumerate(priorities)]
  answer = 0
  while True:
    cur = queue.pop(0)
    if any(cur[1] < q[1] for q in queue):
      queue.append(cur)
    else:
      answer += 1
      if cur[0] == location:
        return answer 
      
print(solution2([1,1,9,1,1,1], 0))