from typing import List

# 버블정렬
def bubble_sort(case: List[int]) -> List[int]:
    for idx in range(len(case)):
        for i in range(len(case) - 1):
            if case[i] > case[i + 1]:
                case[i], case[i + 1] = case[i + 1], case[i]
    return case

print(bubble_sort(case = [5, 6, 3, 4, 2, 1]))

# 삽입정렬
def insertion_sort(case: List[int]) -> List[int]:
    for idx in range(1, len(case)):
        current = case[idx]
        flag = idx - 1
        for i in range(len(case) - flag - 1):
            while flag >= 0 and current < case[flag]:
                case[flag + 1] = case[flag]
                flag -= 1
            case[flag + 1] = current
    return case

print(insertion_sort(case = [5,6,7,8,3,4,1]))

# 선택정렬
def selection_sort(case: List[int]) -> List[int]:
    for idx in range(len(case)):
        min_num = case[idx]
        min_idx = idx
        for i in range(idx, len(case)):
            if case[i] < min_num:
                min_num = case[i]
                min_idx = i
        case[idx], case[min_idx] = case[min_idx], case[idx]
    return case

print(selection_sort(case = [6, 4, 5, 2, 1, 8, 9, 7]))

