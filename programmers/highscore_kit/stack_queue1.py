# 프로그래머스 고득점kit 
# stack/queue - 기능개발

# progresses: 배포 순서대로 각 작업의 진행도를 표시, 정수 배열 (len < 100) 
# speeds: 각 작업의 개발속도를 표시, 정수배열 (len < 100)
# answer: 몇개의 기능이 배포되는지 표시 
# 배포는 하루에 한번만 할 수 있으며 하루의 끝에서 수행된다. 
def Solutions(progresses, speeds):
  answer = []
  day = 0
  count = 0
  while len(progresses):
    if progresses[0] + day * speeds[0] >= 100:
      speeds.pop(0)
      progresses.pop(0)
      count += 1
    else:
      if count > 0:
        answer.append(count)
        count = 0
      day += 1
  answer.append(count)
  return answer

# 입출력 예시 
# progresses	/   speeds	 /   return
# [93, 30, 55] /	[1, 30, 5] /  [2, 1]
# [95, 90, 99, 99, 80, 99]	/  [1, 1, 1, 1, 1, 1]  / 	[1, 3, 2]

print(Solutions([93, 30, 55],[1, 30, 5]))

# 1) 모든 풀이 과정을 다 리스트에 담아두는 방식으로 접근하지 x --> 원하는대로 구현이 안되기 쉽상. 

# 2) 입출력 순서에 대한 언급이 있다면, stack , queue 이라 간파하고 pop 으로 풀려고 해보기 

# 3) stack 의 경우에는 별도의 리스트 만들고 (stack_list)
#   반복하며 stack_list.pop() 으로 접근하면 쉽게 풀림 ex) () {} 문제들. 

# 4) queue 의 경우는 pop(0)