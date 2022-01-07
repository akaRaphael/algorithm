# 프로그래머스 고득점 kit - Greedy
# 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860


# 알파벳 = 26개 

# 기본 시작은 A 부터 시작임 
# 아스키 번호, A가 시작점, 몇번 조작했는지 count 필요 
# 한 글자 완성할 때마다 알파벳과 조작횟수를 엮어줘야함 
# A를 시작으로 역방향과 정방향 중 어떤 방향이 조작횟수가 적은지 비교해야함
# 최소 조작횟수를 찾아야함 

# 좌우를 역방향으로 움직이는게 더 최소인 경우는? 
# => 가운데 글자가 A인 경우 즉, 좌측으로 이동했을 때 마지막 문자로 이동이 가능한 위치 
# => 예를 들어서  JANENNO의 경우, 탐색을 역순으로 가야함.
# => 즉, A가 index 1번자리에 나오면 탐색이 역순이어야 함.

def solution(name):
  start = 65
  end = 90
  move = 0
  answer = []
  
  for idx, char in enumerate(name):
    letter = ord(char)
 
    if idx < len(name) - 1:
      move = 1
    else: 
      move = 0
      
    if (letter - start) > (end - letter + 1):
      answer.append(end - letter + 1 + move)
    else:
      answer.append(letter - start + move)
      
    # if len(name[idx + 1:]) == 2:
    #   if name[idx + 1] == 'A':
    #     last = ord(name[-1])
    #     if (last - start) > (end - last + 1):
    #       answer.append(end - last + 1)
    #       break
    #     else:
    #       answer.append(last - start)
    #       break
  
  print(answer)
  return sum(answer)

print(solution("JEROEN"))

   