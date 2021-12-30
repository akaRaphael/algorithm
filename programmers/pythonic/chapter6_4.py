# 가장 많이 등장하는 알파벳 찾기
# https://programmers.co.kr/learn/courses/4008/lessons/13246

my_str = 'dfdefdgf'

# collections.Counter 를 사용하면 리스트 내의 동일한 원소의 갯수를 알 수 있다.
# Counter는 dict 형태로 원소값을 key로, 갯수를 value로 정리한다.
# 그러나, Counter(dict) 형태로 값을 반환하기 때문에, 반드시 dict 형태로 변환해야 한다.
from collections import Counter
my_str = dict(Counter(my_str))
max_num = max(my_str.values())
result = sorted([key for key, value in my_str.items() if value == max_num])
answer = "".join(result)
print(answer)