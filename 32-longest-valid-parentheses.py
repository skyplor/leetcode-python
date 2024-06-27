class Solution:
  def longestValidParentheses(self, s: str) -> int:
    stack = [-1]
    res = 0
    for i, c in enumerate(s):
      if c == '(':
        stack.append(i)
      else:
        stack.pop()
        if len(stack) == 0:
          stack.append(i)
        else:
          res = max(res, i - stack[-1])
          
    return res

sol = Solution()
# s = "(()"
s = ")()())"
# s = ""
# s = "()(()"
print(f'output: {sol.longestValidParentheses(s)}')