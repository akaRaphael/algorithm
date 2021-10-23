# array를 구현해보자.

# array 생성
array1 = [1, 2, 3]

# 맨 뒤에 요소 추가
array1.append(4) 
print(array1)

# 맨 앞에 요소 추가
# insert(index, data)
array1.insert(0, 0)
print(array1)

# n번째 위치에 요소 추가 
array1.insert(5, 5)
print(array1)
array1.insert(10,10) #요소가 순차적으로 추가되기에 10번째 위치에 넣고 싶어도 array의 마지막 위치에 추가된다.
print(array1)

# 특정 요소의 index 위치 검색 
print("요소 1의 위치 =", array1.index(1))

# 6) 특정 위치의 요소 검색 
print("index 3번 요소 =", array1[3])

# index 기반 삭제 
del array1[0]
print(array1)

# 요소 기반 삭제 
array1.remove(10)
print(array1)
