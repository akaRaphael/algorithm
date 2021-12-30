# map 함수 응용하기
# https://programmers.co.kr/learn/courses/4008/lessons/13252

mylist = [[1,2], [3,4],[5]]
def solution(mylist):
    answer = list(map(len, mylist))
    return answer

print(solution(mylist))