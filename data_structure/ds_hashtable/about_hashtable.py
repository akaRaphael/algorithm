# 1) Hash Table 이란?
#  - key와 value를 한 쌍으로 저장하는 자료구조다. (파이썬의 dictionary와 같은 형태)
#  - Hash Table은 value를 찾기 위해서 그냥 key가 아닌 Hash key를 이용하여 검색한다. 

# 2) Hash key 란?
#  - Hash key는 key 값을 hash 함수에 넣어 반환된 값이다. 
#  - Hash 함수는 임의의 값을 고정된 길이의 값으로 변환한다. 
#  - Hash key는 Hash value, Hash address 라 불리기도 한다. 

# 3) Hash Table의 장점
#  - Hash key값을 이용해 value를 찾기에, 검색에 용이하다.(빠르다)
#  - 각 value는 고유한 hash key를 갖기 때문에 중복 데이터의 검증이 쉽다.

# 4) Hash Table의 단점 
#  - Hash 값(key)의 중복(= Hash Collision)을 피하기 위해 필요이상의 저장공간을 사용한다.
#  - 이처럼 Hash Collision을 피하기 위한 별도의 전략이나 자료구조를 필요로 한다.

# 5) 공간을 탐색시간과 맞바꾼다. 
#  - Hash Table은 필요한 공간보다 더 많은 공간을 사용한다. 
#  - 그러나 저장공간을 더 내어주는 것에 비해 검색효율이 매우 우수하다.
#  - 즉, 검색의 측면에서 저장공간을 더 사용한다는 손해보다 이득이 더 크다는 뜻이다.

# 6) Hash Table의 사용
#  - 검색, 저장, 삭제가 빈번한 경우
#  - 캐시 구현시 활용(중복 검증이 쉽고 빠르기 때문)

# 7) Hash Collision 해결방법 
#  a. Chaining 기법 
#  - Open Hashing 기법 중 하나
#  - Hash Table 저장공간 이외의 공간을 활용하는 방법 
#  - 충돌이 발생한 Hash 값에 연결리스트를 이용하여 데이터를 추가로 저장하는 방법
#  - 그러나 추가적인 공간을 필요로 한다는 단점이 있다. 

#  b. Linear Probing 기법 
#  - Close Hashing 기법 중 하나
#  - Chaning 기법을 보완한 형태 
#  - hash 충돌이 발생하면, Hash Table의 다른 빈공간을 찾아 저장하는 방법 
#  - Hash Table의 공간활용성을 높인다. 