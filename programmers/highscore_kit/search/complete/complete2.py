# 프로그래머스 고득점kit - 완전탐색
# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839

numbers = "011"

# 내가 짠 코드 

# 1) 주어진 문자열들로 만들 수 있는 조합을 우선 다 만들자 => 순열 
# 2) 순열에는 1자리수가 없으므로, 1자리 수를 추가한다.
# 3) set을 이용하여 중복된 값을 제거한다.
# 4) 소수만 찾아서 result에 저장한다. 
# 5) result의 길이를 반환한다. 
# ==> 테스트 예제는 맞았는데, 테스트 케이스 중 틀린 것들이 있다. 
# ==> 아무리 생각해도 이유를 모르겠다.... 

from itertools import permutations
import math

def solution(numbers):
  per_numbers = list(permutations(numbers))
  per_numbers = [int("".join(number)) for number in per_numbers]
  
  for number in numbers:
    per_numbers.append(int(number))
  
  per_numbers = set(per_numbers)
  result = []
  
  for case in per_numbers:
    flag = True
    if case > 1:
      for i in range(2, int(math.sqrt(case)) + 1):
        if case % i == 0:
          flag = False
          break
      if flag:
        result.append(case)
        
  return len(result)
  

# 다른 사람의 솔루션 (https://www.youtube.com/watch?v=m3kCKV8oc1g)
# => 에라토스테네스의 체 알고리즘을 사용한다.

def solution2(numbers):
  prime_set = set()
  
  # 1) 순열 만들기 
  for i in range(len(numbers)): # number의 길이 = 생성가능한 최대 자리수 
    perm = permutations(list(numbers), i + 1) # 자릿수 별로 모든 순열을 생성 
    perm_list = map(int, map("".join, perm))
    prime_set |= set(perm_list)
    
  # 2) 소수 찾기 
  prime_set -= set(range(0, 2)) # 0~2 까지 제외하기 
  
  # 2-1) 에라토스테네스의 체  
  lim = int(max(prime_set) ** 0.5) + 1 # 1을 더하는 이유는 range로 사용하기 위함 
  
  for i in range(2, lim):
    prime_set -= set(range(i * 2, max(prime_set) + 1, i)) 
    # i = 2일때 4부터(2까지는 set에 없음 위에서 제거함), 가장 큰수 까지, 2씩 증가(2배수).
    # i = 3일때 6부터, 가장 큰 수까지, 3씩 증가
    # ==> 이렇게 만든 set은 2,3,4... 배수들이고 여기에 해당하는 수는 제거된다. 
  return len(prime_set)


# 다른 사람의 솔루션 
# => 재귀적 풀이 (https://www.youtube.com/watch?v=m3kCKV8oc1g)

# 1) prime_set을 정의한다. 
prime_set = set()

def is_prime(number):
  # 6) 0과 1을 제외한다
  if number in (0,1):
    return False
   
  # 7) 에라토스테네스의 체 
  lim = int(number**0.5) + 1
  for i in range(2, lim):
    if number % i == 0:
      return False
    
  return True

def recursive(combination, others): # combination = 지금까지 사용한 숫자 / others = 사용하지 않은 숫자 
  # 5) 탈출조건, 지금까지 만들어진 조합이 소수인지 확인한다. 
  if combination != "":
    if is_prime(int(combination)):
      prime_set.add(int(combination))
    
  # 4) 현재까지 만들어진 숫자에 남아있는 숫자 중 하나를 더해준다. 
  for i in range(len(others)):
    recursive(combination + others[i], others[:i] + others[i+1:])
    # combination = combination + others[i] 
    # others = others[:i] + others[i+1:] ==> others의 i번째 요소를 사용했으니까 i번째를 뺀 나머지가 others가 된다. 

def solution3(numbers):
  # 2) 모든 조합을 만드는 recursive를 수행한다. 
  recursive("", numbers) # 최초에는 combination이 비어있고 others기 numbers인 상태 
  
  # 3) prim_set의 length를 반환한다. 
  return len(prime_set)

print(solution3(numbers))