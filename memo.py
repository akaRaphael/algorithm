from typing import List

# 버블정렬
def bubble_sort(case: List[int]) -> List[int]:
    for idx in range(len(case) - 1):
        for i in range(len(case)- idx - 1):
            if case[i] > case[i + 1]:
                case[i], case[i + 1] = case[i + 1], case[i]
    return case

# ==================================================================
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

# ==================================================================
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

# ==================================================================
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
# ==================================================================
import random

def quick_select(case: List[int], k: int) -> int:
    length = len(case)
    if length == 1:
        return case[0]

    pivot_idx = random.randrange(length)
    last_idx = length - 1

    case[pivot_idx], case[last_idx] = case[last_idx], case[pivot_idx]
    pivot = case[-1]
    left_idx = 0
    right_idx = length - 2

    while left_idx <= right_idx: 
        if case[left_idx] <= pivot:
            left_idx += 1
            continue

        if case[right_idx] > pivot:
            right_idx -= 1
            continue

        if pivot < case[left_idx] and pivot >= case[right_idx]:
            case[left_idx], case[right_idx] = case[right_idx], case[left_idx]
            continue

    case[left_idx], case[last_idx] = case[last_idx], case[left_idx]

    if left_idx == length - k:
        return case[left_idx]

    elif left_idx < length - k:
        return quick_select(case = case[left_idx + 1:], k = k)
    
    elif left_idx > length - k:
        return quick_select(case = case[:left_idx], k = k - (length - left_idx))
    
print(quick_select(case = [4, 3, 5, 1, 6, 7], k = 2))