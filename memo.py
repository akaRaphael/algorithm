# 버블정렬
from typing import List
from sys import stdin
input = stdin.readline

def bubble_sort(case: List[int]) -> List[int]:
    for idx in range(len(case) - 1):
        for i in range(len(case) - idx - 1):
            if case[i] > case[i + 1]:
                case[i], case[i + 1] = case[i + 1], case[i]
    return case

print(bubble_sort(case = [5,4,3,2,1]))

# 삽입정렬
def insertion_sort(case: List[int]) -> List[int]:
    for idx in range(1, len(case)):
        current = case[idx]
        flag = idx - 1
        while flag >= 0 and current < case[flag]:
            case[flag + 1] = case[flag]
            flag -= 1
        case[flag + 1] = current
    return case

print(insertion_sort(case = [5,4,3,2,1]))