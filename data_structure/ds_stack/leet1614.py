# 1614. Maximum Nesting Depth of the Parentheses

def maxDepth(s: str) -> int: # 내가 풀은 방법 
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
print(maxDepth(s = "1"))
print(maxDepth(s = "()"))
print(maxDepth(s = ""))

def maxDepth2(s: str) -> int: #stack을 이용한 방법 
  max_depth = 0
  stack = []
  
  for i in range(len(s)):
    if s[i] == "(":
      stack.append("(")
      if len(stack) > max_depth:
        max_depth = len(stack)
        
    elif s[i] == ")":
      stack.pop()
  return max_depth

print(maxDepth2(s = "(1+(2*3)+((8)/4))+1"))
print(maxDepth2(s = "1"))
print(maxDepth2(s = "()"))
print(maxDepth2(s = ""))
    