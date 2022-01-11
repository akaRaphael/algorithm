# 프로그래머스 고득점 kit - Greedy
# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

# 문자열의 순서를 지킨 상태에서 가장 큰 수를 만드는 조합을 찾아야 한다. 

#내가 짠 코드 
from itertools import permutations

number = "4177252841"
k = 4

def solution(number, k):
  
  print(max(number))
  
  
print(solution(number, k))