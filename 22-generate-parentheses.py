from typing import List

class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    # only add open if open_count < n
    # only add closing if closed_count < open
    # valid and return if open_count == closed_count == n
    stack = []
    res = []
    
    def backtrack(open_n, closed_n):
      if open_n == closed_n == n:
        res.append("".join(stack))
        return

      if open_n < n:
        stack.append('(')
        backtrack(open_n + 1, closed_n)
        stack.pop()

      if closed_n < open_n:
        stack.append(')')
        backtrack(open_n, closed_n + 1)
        stack.pop()

    backtrack(0, 0)
    return res

sol = Solution()
input = 3
output = sol.generateParenthesis(input)
print(f'input: {input}\noutput: {output}')