# 1614. Maximum Nesting Depth of the Parentheses

def maxDepth(s: str) -> int:
  max_depth = 0
  depth = 0
  for i in range(len(s)):
    if s[i] == "(":
      depth += 1
    elif s[i] == ")":
      depth -= 1
    max_depth = max(max_depth, depth)
  return max_depth

print(maxDepth(s = "(1+(2*3)+((8)/4))+1"))
    