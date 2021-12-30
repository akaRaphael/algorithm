# 2차원 리스트를 1차원 리스트로 만들기
# https://programmers.co.kr/learn/courses/4008/lessons/13189

# 2차원 리스트의 각 요소를 합쳐 1차원 리스트로 만들기 위해서 
# 일반적으로 다음과 같은 코드를 사용한다. 

mylist = [['A', 'B'], ['X', 'Y'], ['1', '2']]

def solution(mylist):
  answer = []
  for data in mylist:
    answer += data
  return answer

# 그러나 python에는 이를 손쉽게 해결해주는 메소드가 여러개 있다.
# 1) sum
print(f"sum => {sum(mylist, [])}")

# 2) itertools.chain
import itertools
print(f"itertools.chain => {list(itertools.chain.from_iterable(mylist))}")

# 3) itertools & unpacking
print(f"itertools.chain & unpacking => {list(itertools.chain(*mylist))}")

# 4) list comprehension
print(f"list comprehension => {[element for array in mylist for element in array]}")

# 5) functools.reduce
from functools import reduce
print(f"functools.reduce => {list(reduce(lambda x, y : x + y, mylist))}")

# 6) functools.reduce & operator
import operator
print(f"functools.reduce & operator => {list(reduce(operator.add, mylist))}")