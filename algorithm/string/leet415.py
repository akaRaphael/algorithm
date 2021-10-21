class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    answer = []
    carry = 0
    index1, index2 = len(num1), len(num2)
    while index1 or index2 or carry:
      digit = carry
      if index1:
        index1 -= 1
        digit += int(num1[index1])
      if index2:
        index2 -= 1
        digit += int(num2[index2])

      carry = digit > 9 
      answer.append(str(digit % 10))
    return "".join(answer[::-1]) # ::-1 은 배열의 처음부터 끝까지 역순으로 읽으라는 뜻이다.

f = Solution()
print(f.addStrings("11", "11"))