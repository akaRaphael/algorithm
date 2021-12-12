# Linear probing 기법 구현

hash_table = [None] * 8

def get_key(key):
  return hash(key)

def hash_function(key):
  return key % 8

def store(key, value):
  index_key = get_key(key)
  hash_address = hash_function(index_key)
  
  if hash_table[hash_address] != None:
    for i in range(hash_address, len(hash_table)):
      if hash_table[i] == None: # 해당 위치에 데이터가 존재하지 않는 경우 
        hash_table[i] = [index_key, value]
        return
      elif hash_table[i][0] == index_key: # 해당 위치에 동일한 키가 존재하는 경우 
        hash_table[i][1] = value # 기존의 value를 새로운 value로 변경
        return
  else:
    hash_table[hash_address] = [index_key, value]
    
def read(key):
  index_key = get_key(key)
  hash_address = hash_function(index_key)
  
  if hash_table[hash_address] != None:
    for i in range(hash_address, len(hash_table)):
      if hash_table[i] == None:
        return "There is no matching value with the key."
      elif hash_table[i][0] == index_key:
        return hash_table[i][1]
  else:
    return "None" 
  
store("Raphy", 123)
store("Mike", 456)
print(hash_table)
print(read("Raphy"))
print(read("Mike"))
print(read("Raphael"))
  
        
    
    