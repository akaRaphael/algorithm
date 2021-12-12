# chaining 기법 구현 
hash_table = [None] * 8

def get_key(data):
  return hash(data)

def hash_function(key):
  return key % 8

def store(key, value):
  index_key = get_key(key)
  hash_address = hash_function(index_key)
  
  if hash_table[hash_address] != None: # 배열의 해당 index에 data가 존재한다면 
    # 연결리스트이므로, 다수의 데이터가 존재할 수 있기 때문에 반복문으로 key값을 검색하기 위함 
    for i in range(len(hash_table[hash_address])): 
      if hash_table[hash_address][i][0] == index_key: # 해당 key가 이미 존재하는 경우
        hash_table[hash_address][i][1] = value # 해당 key에 할당된 value 값을 변경
        return
    # 배열의 해당 index에 다수의 데이터는 존재하지만 hash key값이 중복되지 않는 경우   
    hash_table[hash_address].append([index_key, value])
  else:# 아무 데이터도 존재하지 않는 경우 
    hash_table[hash_address] = [[index_key, value]]
    
def read(key):
  index_key = get_key(key)
  hash_address = hash_function(index_key)
  
  if hash_table[hash_address] != None:
    for i in range(len(hash_table[hash_address])):
      if hash_table[hash_address][i][0] == index_key:
        return hash_table[hash_address][i][1]
    return "There is no matching value with the key."
  else:
    return "None"
    
store("Raphy", 123)
store("Mike", 456)
print(hash_table)
print(read("Raphy"))
print(read("Mike"))
print(read("Raphael"))