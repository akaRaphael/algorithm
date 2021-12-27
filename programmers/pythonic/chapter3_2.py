# 알파벳 출력하기
# https://programmers.co.kr/learn/courses/4008/lessons/13340

num = int(input().strip())

# 내가 짠 코드 
alphabet = 'abcdefghijklmnopqrstuvwxyz'

if num == 1:
  print(alphabet.upper())
elif num == 0:
  print(alphabet.lower())
  
# pythonic한 코드
import string
 
if num == 1:
  print(string.ascii_uppercase)
elif num == 0:
  print(string.ascii_uppercase)