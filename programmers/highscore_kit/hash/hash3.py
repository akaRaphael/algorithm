# 프로그래머스 고득점 kit - hash
# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

# 입출력 예시
# input / result 
# [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]] / 5
# [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]] / 3

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]] 

def solution(clothes):
  category = {}
  result = 1
  for cloth in clothes:
    key = cloth[1]
    item = cloth[0]
    if key in category:
      category[key].append(item)
    else:
      category[key] = [item]

  for key in category.keys(): # 1을 더하는 이유는 아예 안입는 경우 때문이다. 
    result = result * (len(category[key]) + 1)
  
  return result - 1 # 1을 마지막에 빼는 이유는 어떤 옷도 안입는 경우를 제외하는 것이다. 

print(solution(clothes))
  

# 프로그래머스에서 가장 좋아요가 많은 솔루션 
def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    print(cnt.values())
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
  
print(solution2(clothes))