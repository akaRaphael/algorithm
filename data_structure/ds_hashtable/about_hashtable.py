# 1) HashTable 이란?
# - key와 value로 구성된 자료구조
# - key를 value에 indexing 할 때, hash function을 사용하여 key값을 변환한다.
# - 이 과정을 Hashing 이라고 한다. 
# - Hashing 과정을 사용하여 key와 value의 형태로 자료를 저장하는 형태를 Hash Table이라고 한다.

# 2) HashTable의 장점
# - 배열처럼 index를 사용하여 특정 값을 검색하기 때문에, 데이터 저장 및 검색에 용이하다.
# - Hash key를 사용하기 때문에 데이터의 중복성 검사가 용이하다. 

# 3) HashTable의 단점
# - Hash key를 사용하기위해 더 많은 저장공간을 필요로한다.
# - Hash key 값의 중복을 해결하기 위한 별도의 자료구조 및 저장방식이 필요하다.

# 4) HashTable의 특성 - 공간과 시간을 맞바꾸는 기법 
# - Hash key를 사용하기 위해 추가적으로 필요로하는 저장공간에 비해 시간적 효율이 좋다는 의미다.
# - HashTable은 Hash key를 사용하기 위해 저장할 데이터보다 더 많은 공간을 필요로 한다.
# - 그러나 추가적으로 사용하는 저장공간에 비해 검색/탐색 속도가 매우 우수하기에 붙여진 표현이다.

# 5) Hash Collision이란?
# - Hashing 으로 생성된 Key값이 중복되는 현상 

# 6) Hash Collision 해결책 - Chaining 기법 
# - Open Hashing 기법 중 하나
# - 연결리스트를 사용하여 중복되는 key에 해당하는 데이터를 여러개 관리하는 방법
# - 연결리스트라는 추가적인 자료구조 및 공간을 사용하는 것이 단점으로 꼽힌다. 

# 7) Hash Collision 해결책 - Linear Probing
# - Close Hasing 기법 중 하나 
# - 중복되는 key에 해당하는 데이터를, HashTable의 다음 빈공간에 저장하는 방법 
# - Hash Table의 공간낭비를 최소화하는 방법이자, Chaining기법의 보완책 
# - Hash Table의 저장공간 활용도를 높이는 방법

# 7-1) Linear Probing의 문제점 
# - hash value는 다르지만 동일한 index 값을 가지는 경우, 
# - hash table의 그 다음 빈자리에 값을 추가하는 방식으로 동작한다. 
# - 그러나 여기서 한가지 예외상황이 발생한다. 
# - 만약 8의 길이를 갖는 hash table의 index 7번(끝자리)에 데이터가 존재하는 경우 
# - 기존의 index 7번의 데이터와는 다른 hash value를 가진 새로운 데이터를 삽입하려고 한다면, 
# - Linear Probing의 규칙에 따라 8번째 자리에 새로운 데이터가 삽입되어야 한다.
# - 하지만, 해당 hash table은 7번 index 까지만 존재하기에 8번째 자리에 새로운 데이터 삽입이 불가하다.
# - 이 경우, 새로운 데이터가 저장되지 않는 문제가 발생한다.  

# 7-2) Clustering(클러스터링)
# - 7-2에서 설명한 문제점이 바로 클러스터링이다.
# - 클러스터링의 사전적 의미는 비슷한 특성을 가진 데이터의 집합을 의미한다. 
# - 여기서는 동일한 또는 근사한(approximate) 테이블 index를 갖는 key들이 뭉쳐있는 상태를 말한다.
# - 클러스터링이 발생하면, 데이터의 검색 및 탐색 속도가 길어지게 되며 7-2에서 말한 문제점이 발생할 수 있다.
# - 이를 보완한 Quadratic Probing, Double Hashing 기법이 있다.