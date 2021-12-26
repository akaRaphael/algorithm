# 몫과 나머지
# https://programmers.co.kr/learn/courses/4008/lessons/13323

# 내가 짠 코드 
# a, b = map(int, input().strip().split(' '))
a, b = 5, 3
print(a//b, a%b)

# pythonic한 코드 
print(divmod(a, b))
print(*divmod(a, b)) # unpacking - divmod는 tuple을 반환하므로 unpacking을 통해 풀어낸다.

# 1. divmod
# - 파이썬의 내장함수로, 2개의 숫자를 입력받아 목과 나머지를 튜플 형태로 반환한다.
# - 즉, a//b와 a%b를 수행한다. 

# a. divmod 주의사항)
# - 두번째 인자에 0을 넣는 경우, ZeroDivisionError가 발생한다. 
# - 그러므로 두번째 인자에 0을 할당하지 않도록 주의해야한다.  
# - divmod는 작은 수를 대상으로 수행할 때에는 //와 %보다 느리다.
# - 다만, 큰 수를 대상으로 수행할 경우 더 빠르다. 


# 2. packing
# - packing은 여러개의 객체를 하나의 객체로 합쳐주는 기능이다. 
# - packing에는 2가지가 존재한다.

# a) 위치인자 packing 
# - print('a', 'b', 'c')
# - print 함수는 매개변수의 갯수에 대한 제약이 없다. 이것이 가능한 이유가 packing이다. 
# - 즉, 함수의 인자(=매개변수)의 갯수를 유연하게 지정할 때 사용한다.
# - 위치인자(*)를 매개변수 앞에 붙이면 packing을 사용한다. 
# - 위치인자를 사용하면 다수의 값들을 tuple로 관리한다. 
 
# 예시 - 위치인자) 
def test_packing(*args):
  print(type(args))
  print(args)
test_packing(1,2,3,4,5)

# b) 키워드인자 packing 
# - 키워드 인자는 **을 사용해 표시할 수 있다. 
# - key와 value로 구성된 다수의 값을 dictionary로 관리한다. 

# 예시 - 키워드인자 
def kwpacking(**kwargs):
  print(type(kwargs))
  print(kwargs)
kwpacking(a=1, b=2, c=3)


# 3. unpacking
# - packing은 여러개의 객체를 하나의 객체로 합쳐주는 기능이다. 
# - 반대로 unpacking은 여러개의 객체로 합쳐진 하나의 객체를 풀어내는 기능이다. 
# - unpacking을 하기 위해서는 위치인자(*) 또는 키워드인자(**)를 붙여주면 된다. 
# - Container 타입의 객체라면 unpacking이 가능하다. 

# 예시 - unpacking 
def sum(a, b, c):
  return a + b + c

numbers = [1,2,3]
# print(sum(numbers)) 
# => numbers는 packing 되어있는 객체로, sum함수의 매개변수 갯수에 맞지 않다. 
print(sum(*numbers)) # unpacking 

# sum(*numbers) == sum(*[1,2,3]) == sum(1,2,3)
# 이 세가지는 모두 의미를 갖는다. 