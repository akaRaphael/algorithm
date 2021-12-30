# 곱집합(Cartesian product) 구하기 - product
# https://programmers.co.kr/learn/courses/4008/lessons/12835

# 다수의 리스트 원소간 조합의 모든 경우의 수를 구하기 위해서는 
# 일반적으로 이를 구하기 위해서는 다음과 같은 다중 for문을 사용한다. 
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)

# 그러나 python 에서는 itertools 라이브러리에 product 라는 함수를 사용하면 된다.
# 위에서 사용한 다중 for문과 동일한 결과를 출력한다. 

import itertools
print(list(itertools.product(iterable1, iterable2, iterable3)))