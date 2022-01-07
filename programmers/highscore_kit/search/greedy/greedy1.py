# 프로그래머스 고득점 kit - Greedy
# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

n = 5
lost = [1,3,5]
reverse = [2,3,5]

# 나의 풀이 
# 케이스를 나누면 다음과 같다.
# 여분의 체육복이 있는 학생
# 여분의 체육복이 없는 학생
# 체육복이 아예 없는 학생 
# 핵심은 여벌의 체육복을 가진 학생이 도난을 당한 경우를 생각해야한다. 

def solution(n, lost, reverse):
  new_lost = set(lost) - set(reverse)
  new_reverse = set(reverse) - set(lost)
  student = n - len(new_lost)
  for number in new_reverse:
    before = number - 1
    after = number + 1
    if before in new_lost:
      student += 1
      new_lost.remove(before)
    elif after in new_lost:
      student += 1
      new_lost.remove(after)
  return student
print(solution(n, lost, reverse))

# 프로그래머스에서 최다 좋아요 솔루션 
def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
