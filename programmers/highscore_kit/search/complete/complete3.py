# 프로그래머스 고득점kit - 완전탐색
# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

# 입출력 예
# brown	/ yellow / return
# 10 / 2 / [4, 3]
# 8	/ 1	/ [3, 3]
# 24 / 24 /	[8, 6]

brown = 24
yellow = 24

# 내가 짠 코드 ==> 통과 
# yellow가 몇줄이냐에 따라서 brown의 갯수를 구하면 된다. 
def solution(brown, yellow):
  yellow_line = 1
  while True:
    if yellow % yellow_line == 0:
      width = (yellow // yellow_line) + 2
      height = yellow_line + 2
      count_brown =  height * width - yellow 
      if brown == count_brown:
        break
      
    yellow_line += 1
    
  return [width, yellow_line + 2]
    
print(solution(brown, yellow))

