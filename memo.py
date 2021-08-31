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

# 병합정렬
def merge_sort(case: List[int]) -> List[int]:
    length = len(case)

    if length == 1:
        return case
    
    mid = length // 2

    left_case = case[:mid]
    right_case = case[mid:]

    sorted_left = merge_sort(case = left_case)
    sorted_right = merge_sort(case = right_case)

    sorted_case = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(sorted_left) or right_idx < len(sorted_right):

        if left_idx == len(sorted_left):
            sorted_case.append(sorted_right[right_idx])
            right_idx += 1
            continue

        if right_idx == len(sorted_right):
            sorted_case.append(sorted_left[left_idx])
            left_idx += 1
            continue

        if sorted_right[right_idx] <= sorted_left[left_idx]:
            sorted_case.append(sorted_right[right_idx])
            right_idx += 1

        else:
            sorted_case.append(sorted_left[left_idx])
            left_idx += 1
    
    return sorted_case


print(bubble_sort(case = [6, 4, 1, 3, 2, 1, 7]))
print(insertion_sort(case = [6, 4, 1, 3, 2, 1, 7]))
print(selection_sort(case = [6, 4, 1, 3, 2, 1, 7]))
print(merge_sort(case = [8, 7, 6, 5, 4, 3, 2, 1]))
