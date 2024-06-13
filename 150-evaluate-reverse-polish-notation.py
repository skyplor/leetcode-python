from typing import List

class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    # stack - []
    # operand requires minimum of 2 numbers so we will pop 2 numbers
    # if-else for operands
    stack = []
    for token in tokens:
      if token.lstrip('-').isdigit():
        stack.append(int(token))
      else:
        num_1 = stack.pop()
        num_2 = stack.pop()
        if token == '+':
          stack.append(num_2 + num_1)
        elif token == '-':
          stack.append(num_2 - num_1)
        elif token == '*':
          stack.append(num_2 * num_1)
        else:
          stack.append(int(num_2 / num_1))
          
    return stack.pop()
  
sol = Solution()
# input = ["2","1","+","3","*"]
# input = ["4","13","5","/","+"]
input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
output = sol.evalRPN(input)
print(f'Input: {input}\nOutput: {output}')