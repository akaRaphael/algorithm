# 1021. Remove Outermost Parentheses

def remove(s:str) -> str:
  result = ""
  stack = []
  for i in s:
    if i == "(":
      if stack:
        result += i
      stack.append(i)
    else:
      stack.pop()
      if stack:
        result += i
  return result
  
print(remove( s = "(()())(())"))
print(remove( s = "()()"))
print(remove( s = "(()())(())(()(()))"))
