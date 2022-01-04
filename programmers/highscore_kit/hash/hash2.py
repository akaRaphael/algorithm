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

# 프로그래머스에서 좋아요가 가장 많은 솔루션 
def solution2(phone_book):
  phone_book = sorted(phone_book)
  for p1, p2 in zip(phone_book, phone_book[1:]):
    if p2.startswith(p1):
      return False
  return True

print(solution2(phone_book))