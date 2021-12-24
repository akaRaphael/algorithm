# 프로그래머스 고득점kit 
# stack/queue - 기능개발

# progresses: 배포 순서대로 각 작업의 진행도를 표시, 정수 배열 (len < 100) 
# speeds: 각 작업의 개발속도를 표시, 정수배열 (len < 100)
# answer: 몇개의 기능이 배포되는지 표시 

# 배포는 하루에 한번만 할 수 있으며 하루의 끝에서 수행된다.
# 배포 순서대로 작업이 완료되어야 배포를 할 수 있다. 
# 2번 작업이 완료되어도 1번 작업이 완료되지 않으면 배포할 수 없다. 

# 입출력 예시 
# progresses	/   speeds	 /   return
# [93, 30, 55] /	[1, 30, 5] /  [2, 1]
# [95, 90, 99, 99, 80, 99]	/  [1, 1, 1, 1, 1, 1]  / 	[1, 3, 2]

def solution1(progresses, speeds):
  answer = []
  day = 0
  count = 0
  while len(progresses) > 0:
    if progresses[0] + day * speeds[0] >= 100:
      progresses.pop(0)
      speeds.pop(0)
      count += 1
    else:
      if count > 0:
        answer.append(count)
        count = 0
      day += 1
  answer.append(count)
  return answer
print(solution1([93, 30, 55],[1, 30, 5]))

# 가장 많이 좋아요를 받은 풀이 
def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

# Stack / Queue 문제 Tips!!! 
# 1) 모든 풀이 과정을 다 리스트에 담아두는 방식으로 접근하지 x --> 원하는대로 구현이 안되기 쉽상. 
# 2) 입출력 순서에 대한 언급이 있다면, stack , queue 이라 간파하고 pop 으로 풀려고 해보기 
# 3) stack 의 경우에는 별도의 리스트 만들고 (stack_list) 반복하며 stack_list.pop() 으로 접근하면 쉽게 풀림 ex) () {} 문제들. 
# 4) queue 의 경우는 pop(0)