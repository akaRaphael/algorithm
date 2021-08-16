# 백준 단계별 풀이 9단계 - 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085

# x, y, w, h = map(int, input().split())
# right_distance = w - x
# left_distance = x
# top_distance = h - y
# down_distance = y

# result_x = 0
# result_y = 0

# if right_distance >= left_distance:
#   result_x = left_distance
# else:
#   result_x = right_distance

# if top_distance >= down_distance:
#   result_y = down_distance
# else:
#   result_y = top_distance

# if result_x >= result_y:
#   print(result_y)
# else:
#   print(result_x)

############################## 개선된 코드 
x, y, w, h = map(int, input().split())
width_diff = w - x
height_diff = h - y
print(min(x, y, width_diff, height_diff))