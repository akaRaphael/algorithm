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
# - Close Hasing(= open addressing) 기법 중 하나 
# - 중복되는 key에 해당하는 데이터를, HashTable의 다음 빈공간에 저장하는 방법 
# - Hash Table의 공간낭비를 최소화하는 방법이자, Chaining기법의 보완책 
# - Hash Table의 저장공간 활용도를 높이는 방법

# 7-1) Linear Probing의 문제점 1
# - hash value는 다르지만 동일한 index 값을 가지는 경우, 
# - hash table의 그 다음 빈자리에 값을 추가하는 방식으로 동작한다. 
# - 그러나 여기서 한가지 예외상황이 발생한다. 
# - 만약 8의 길이를 갖는 hash table의 index 7번(끝자리)에 데이터가 존재하는 경우 
# - 기존의 index 7번의 데이터와는 다른 hash value를 가진 새로운 데이터를 삽입하려고 한다면, 
# - Linear Probing의 규칙에 따라 8번째 자리에 새로운 데이터가 삽입되어야 한다.
# - 하지만, 해당 hash table은 7번 index 까지만 존재하기에 8번째 자리에 새로운 데이터 삽입이 불가하다.
# - 이 경우, 새로운 데이터가 저장되지 않는 문제가 발생한다.  

# 7-2) Linear Probing의 문제점 2
# - Linear Probing의 경우 삭제시 문제점이 발생하게 된다.
# - 동일한 index 번호를 가지지만 서로다른 hash value를 가진 데이터 3개가 일렬로 저장되어 있다고 해보자.
# - 이를 A1, B1, C1 이라고 할 경우, B1이 삭제되고 나면 Hash table에는 A1, None, C1이 남게 된다.
# - 이 경우, A1은 검색하는데 문제가 발생하지 않지만 C1을 검색할 수 없는 문제점이 발생한다.
# - 이를 방지하기 위해서는 B1을 삭제할 때, 클러스터링을 재정렬하는 알고리즘이 필요하다.  

# 7-3) Clustering(클러스터링)
# - 7-2에서 설명한 문제점이 바로 클러스터링이다.
# - 클러스터링의 사전적 의미는 비슷한 특성을 가진 데이터의 집합을 의미한다. 
# - 여기서는 동일한 또는 근사한(approximate) 테이블 index를 갖는 key들이 뭉쳐있는 상태를 말한다.
# - 클러스터링이 발생하면, 데이터의 검색 및 탐색 속도가 길어지게 되며 7-2에서 말한 문제점이 발생할 수 있다.
# - 이를 보완한 Quadratic Probing, Double Hashing 기법이 있다.

# 8) Quadratic Probing과 Double Hashing 기법 
# - 핵심만 설명하자면, 두 기법 모두 클러스터링을 예방하기 위해 데이터를 띄엄띄엄 저장하는 방법이다.
#   a. Quadratic Probing
#     - Linear Probing과 동일하게 작동하지만, 클러스터링을 예방하기 위해 연속으로 저장되는 데이터의 간격이 넓다.
#   b. Double Hashing
#     - 2가지 종류의 Hash function을 사용하여 1차적으로 hashing된 키가 collision을 일으키는 경우, 
#     - 다른 Hash function을 적용하여 새로운 key를 생성하는 방법 

# 9) 결론
# - 위에서 언급한 Hash table 사용시 발생하는 다양한 문제점을 해결하는 방법이 있다.
#
#   1. Hash table 저장공간의 50% 이상 사용하지 않는다. 
#     => 만약 저장공간의 50% 이상 사용해야 한다면, hash table의 크기를 2배 이상 늘린다.
#
#   2. 고정적인 Hash value를 생성하는 함수를 사용한다. 
#     => hash() 함수는 실행시 매번 다른 hash value를 반환한다. 
#     => 그러므로 다음과 같은 유명한 Hashing 함수를 사용한다. 
#     => SHA-1, SHA-256

# 10) hash table의 시간복잡도
# - 일반적인 경우 (collision이 없는 상태): O(1)
# - 최악의 경우 (collision이 매번 발생): O(n)

# * hash table을 사용한다면, 일반적인 경우에 한해서 사용하기에 
#   hash table의 시간복잡도는 O(1)이라고 말할 수 있다. 
# * 더불어, hash table을 사용함에 있어서 collision은 반드시 제거 해야하는 요소다. 