# chaining 기법 구현 
hash_table = [None] * 8

def get_key(data):
  return hash(data)

def hash_function(key):
  return key % 8

def store(key, value):
  index_key = get_key(key)
  hash_address = hash_function(index_key)
  
  if hash_table[hash_address] != None:
    for i in range(len(hash_table[hash_address])):
      if hash_table[hash_address][i][0] == index_key:
        hash_table[hash_address][i][1] = value
    hash_table[hash_address].append([index_key, value])
  else:
    hash_table[hash_address] = [[index_key, value]]

hash_table = [None] * 8
linked_list = [["key1", "value1"]]
hash_table[0] = linked_list
hash_table[0].append(["key2", "value2"])

print(hash_table)
print(hash_table[0])
print(hash_table[0][0])
print(hash_table[0][1])
print(hash_table[0][0][0])
print(hash_table[0][1][0])
