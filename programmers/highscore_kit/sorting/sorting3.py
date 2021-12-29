# 프로그래머스 고득점 kit - 정렬
# H-index => https://programmers.co.kr/learn/courses/30/lessons/42747

# 입출력 예시 
# citations	/ return
# [3, 0, 6, 1, 5]	/ 3

# n = 논문의 수(위의 예시에서는 5)
# h = 어떤 논문이 인용된 횟수 
# h-index = h번 인용된 논문이 h개인 경우의 최대값 
# ex. 최대 3번 인용된 논문이 3개라면 h-index는 3이 된다.

# 내가 짠 코드 => 실패(원인파악 후 다시 작성함) => 문제 해결했으나 O(n^2)으로 시간복잡도가 안좋다. 
# 예제는 통과했으나 테스트 케이스에서 실패했다.
# 그 이유는 문제 자체를 온전히 이해하지 못했기 때문이다. 
# 예를 들어, [12,11,10,9,8,1]의 논문배열이 있다면 답은 5가 나와야 한다.
# 내가 이해한 내용은 저 원소 중에서 h값을 찾으라는 것이었다. 
# 그게 아니라, 최소값 1부터 최대값 12 중 h-index의 조건을 만족하는 수를 찾는 것이 문제였다. 
 
citations = [12,11,10,9,8,1]

def solution(citations):
  answer = 0
  count = 0
  for i in range(max(citations) + 1):
    for idx in range(len(citations)):
      if i <= citations[idx]:
        count += 1
    if count >= i and i > answer:
      answer = i
    count = 0
  return answer

print(solution([12,11,10,9,8,1]))


# 다른 사람의 솔루션
# 아래 코드에서 이해하지 못한 부분은 n-i, h가 횟수이면서 동시에 논문의 편수(=원소의 갯수)라는 것이다.
# 즉, h-index의 범위는 논문의 갯수(= 원소의 갯수)에 한정되어 있다. 
# 우선 인용횟수를 오름차순으로 정렬한다. [3, 1, 6, 0, 5] => [0, 1, 3, 5, 6]
# n이 3인 경우를 보면, 3번 이상 인용된 논문은 원소 3 다음에 위치한다.
# 배열에서 3, 5, 6이 있기 때문에 3번 이상 인용된 논문은 3편이다. 이는 h-index의 조건에 만족한다. 
# n이 4, 5인 경우는 남은 원소의 갯수가 4와 5 보다 적기 때문에 h-index의 조건에 부합하지 않다. 
def solution2(citations):
  citations.sort()
  n = len(citations)
  for i in range(n):
    if citations[i] >= n - i:
      return n - i
  return 0

print(solution2(citations))


# 프로그래머스에서 가장 좋아요를 많이 받은 솔루션 
def solution3(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
  
  