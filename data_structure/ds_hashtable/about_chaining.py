# Chaining 기법 구현
hash_table = [0 for i in range(10)]

def get_hash(key):
  return hash(key)

def hash_func(key):
  return key % 8 #hash key의 범위는 0 ~ 7