# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840


answers = [1,2,3,4,5]

# 내가 짠 코드 => 통과
def solution(answers):
  answer_length = len(answers)
  candidate1 = [1,2,3,4,5] * answer_length
  candidate2 = [2,1,2,3,2,4,2,5] * answer_length
  candidate3 = [3,3,1,1,2,2,4,4,5,5] * answer_length

  candidate_score = [0,0,0]
    
  for idx, number in enumerate(answers):
    if candidate1[idx] == number:
      candidate_score[0] += 1
      
    if candidate2[idx] == number:
      candidate_score[1] += 1
    
    if candidate3[idx] == number:
      candidate_score[2] += 1
  
  result = []
  max_score = max(candidate_score)
  for idx, score in enumerate(candidate_score):
    if score == max_score:
      result.append(idx + 1)
      
  return result

print(solution(answers))

# 프로그래머스에서 가장 좋아요를 많이 받은 솔루션 
def solution2(answers):
  candidate1 = [1,2,3,4,5]
  candidate2 = [2,1,2,3,2,4,2,5]
  candidate3 = [3,3,1,1,2,2,4,4,5,5]
  score = [0,0,0]
  result = []
  
  for idx, answer in enumerate(answers):
    if answer == candidate1[idx % len(candidate1)]:
      score[0] += 1
      
    if answer == candidate2[idx % len(candidate2)]:
      score[1] += 1
      
    if answer == candidate3[idx % len(candidate3)]:
      score[2] += 1
      
  for idx, s in enumerate(score):
    if s == max(score):
      result.append(idx + 1)
      
  return result

print(solution2(answers))