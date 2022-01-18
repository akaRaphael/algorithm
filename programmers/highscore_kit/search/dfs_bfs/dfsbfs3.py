# 프로그래머스 고득점 Kit - DFS/BFS
# 단어변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

# 입출력 예
# begin	target	words	return
# "hit"	/ "cog"	/ ["hot", "dot", "dog", "lot", "log", "cog"] / 4
# "hit"	/ "cog"	/ ["hot", "dot", "dog", "lot", "log"] /	0

# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.


# 1) BFS 풀이 - https://muhly.tistory.com/86
from collections import deque

def check(s, begin):
    answer = 0
    for i in range(len(s)):
        if list(s)[i] != list(begin)[i]:
            answer += 1
    return True if answer == 1 else False

def solution(begin, target, words):
  if target not in words:
    return 0

  queue = deque()
  queue.append([begin, []])

  while queue:
    n, l = queue.popleft()
    for word in words:
      if word not in l and check(word, n):
        if word == target:
          return len(l) + 1
        temp = l[0:]
        temp.append(word)
        queue.append([word, temp])
  return 0


# 2) DFS 풀이 - https://moseory20.tistory.com/31
def solution2(begin, target, words):
  if target not in words:
    return 0
    
  answer = 0
  word_len = len(begin)
  word_list = [begin]
  diff_word = list()
  
  while(1):
    for wl in word_list:
      diff_word.clear()
      for word in words:
          diff = 0
          for idx in range (0, word_len):
            if wl[idx] != word[idx]: diff += 1
            if diff > 1: break
            
          if diff == 1: # 1글자 차이
            diff_word.append(word)
            words.remove(word)
      
    answer += 1            
    if target in diff_word: 
      return answer
    else: 
      word_list = diff_word


# 3) 프로그래머스 최다 좋아요 솔루션
from collections import deque

def get_adjacent(current, words):
  for word in words:
      if len(current) != len(word):
          continue

      count = 0
      for c, w in zip(current, word):
          if c != w:
              count += 1
              
      if count == 1:
          yield word

def solution(begin, target, words):
  dist = {begin: 0}
  queue = deque([begin])

  while queue:
      current = queue.popleft()
      for next_word in get_adjacent(current, words):
          if next_word not in dist:
              dist[next_word] = dist[current] + 1
              queue.append(next_word)

  return dist.get(target, 0)