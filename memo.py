from typing import List

# 버블정렬
def bubble_sort(case: List[int]) -> List[int]:
    for idx in range(len(case) - 1):
        for i in range(len(case)- idx - 1):
            if case[i] > case[i + 1]:
                case[i], case[i + 1] = case[i + 1], case[i]
    return case

# 삽입정렬
def insertion_sort(case: List[int]) -> List[int]:
    for idx in range(1, len(case)):
        flag = idx - 1
        current = case[idx]
        while flag >= 0 and current < case[flag]:
            case[flag + 1] = case[flag]
            flag -= 1
        case[flag + 1] = current
    return case

# 선택정렬
def selection_sort(case: List[int]) -> List[int]:
    for idx in range(len(case)):
        min_num = case[idx]
        min_idx = idx
        for i in range(idx, len(case)):
            if min_num > case[i]:
                min_num = case[i]
                min_idx = i
        case[min_idx] , case[idx] = case[idx], case[min_idx]
    return case

print(bubble_sort(case = [6, 4, 1, 3, 2, 1, 7]))
print(insertion_sort(case = [6, 4, 1, 3, 2, 1, 7]))
print(selection_sort(case = [6, 4, 1, 3, 2, 1, 7]))
