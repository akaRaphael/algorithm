# 고득점 kit - Heap
# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

# 섞은 음식의 스코빌 지수 = 가장 낮은 스코빌 음식  + (두번째로 낮은 스코빌 음식 * 2)

scoville = [1,2,3,9,10,12]  
k= 7

# 내가 짠 코드 (정답)
import heapq
def solution(scoville, k):
  count = 0
  heapq.heapify(scoville)
  while scoville[0] < k:
    count += 1
    try:  
      first = heapq.heappop(scoville)
      second = heapq.heappop(scoville)
      heapq.heappush(scoville, first + second * 2)
    except:
      return -1 
  return count

print(solution(scoville ,k))    