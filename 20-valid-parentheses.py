class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    for c in s:
      if self.isOpenBracket(c):
        stack.append(c)
      else:
        if not stack:
          return False
        open = stack.pop()
        if not self.isMatched(open, c):
          return False

    return False if stack else True

  def isOpenBracket(self, c: str) -> bool:
    return c in '({['
  
  def isMatched(self, open: str, close: str) -> bool:
    return (
      (open == '(' and close == ')')
      or (open == '{' and close == '}')
      or (open == '[' and close == ']')
    )
    
sol = Solution()
input = '[]()'
output = sol.isValid(input)
print(f'Input: {input}\nOutput: {output}')