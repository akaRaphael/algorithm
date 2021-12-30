# 순열과 조합
# https://programmers.co.kr/learn/courses/4008/lessons/13347

# permutation을 사용하여 순열을 손쉽게 만들 수 있다.

import itertools 

mylist = [1,2,3]
answer = sorted(list(map(list, itertools.permutations(mylist))))
print(answer)

list2 = ['A', 'B', 'C']
print(list(map(list, itertools.permutations(list2))))
print(list(map("".join, itertools.permutations(list2))))