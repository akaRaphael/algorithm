class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if (haystack == "" and needle == "") or needle == "":
      return 0
    elif haystack == "":
      return -1

    split_check = haystack.split(needle)

    if split_check[0] == haystack:
      answer = -1
    elif split_check[0] != haystack:
      answer = len(split_check[0])
    
    return answer

f = Solution()
print(f.strStr("Hello", "ll"))