# 프로그래머스 고득점 kit - hash
# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

phone_book = ["112","456","112345"]

# 내가 짠 코드 => 기본 테스트 코드는 통과 
# - 그러나 시간복잡도아 O(n^2) 이라서 효율성 테스트 실패 
def solution(phone_book):
  phone_book.sort(key = len)
  answer = True
  
  while True:
    prefix = phone_book[0]
    phone_book = phone_book[1:]
    
    for number in phone_book:
      if prefix == number[:len(prefix)]:
        answer = False
        break
    if len(phone_book) == 1:
      break;
  return answer

print(solution(phone_book))

# 다른 사람의 솔루션 => zip
def solution2(phone_book):
  phone_book = sorted(phone_book)
  for p1, p2 in zip(phone_book, phone_book[1:]):
    if p2.startswith(p1):
      return False
  return True

print(solution2(phone_book))

# 다른 사람의 솔루션 => hash
def solution3(phone_book):
  answer = True
  hash_map = {}
  for phone_number in phone_book:
    hash_map[phone_number] = 1
  for phone_number in phone_book:
    temp = ""
    for number in phone_number:
      temp += number
      if temp in hash_map and temp != phone_number:
        answer = False
  return answer

print(solution3(phone_book))