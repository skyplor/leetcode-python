from collections import deque

class Solution:
  def reverseParentheses(self, s: str) -> str:
    '''
    We can use 2 stacks for this
    Stack 1 will store all the characters while reading in including the brackets
    Whenever we encounter a closing bracket, pop all characters from stack 1 until we encounter the first opening bracket
    for each character that we pop, we push them into Stack 2
    Once we encounter an opening bracket, we then pop from stack 2 and push into stack 1, then continue the outside loop
    '''

    mainStack = []
    tempQueue = deque()

    for c in s:
      if c != ')':
        mainStack.append(c)
      else:
        tempC = mainStack.pop()
        while tempC != '(':
          tempQueue.append(tempC)
          tempC = mainStack.pop()

        for _ in range(len(tempQueue)):
          newC = tempQueue.popleft()
          mainStack.append(newC)

    return ''.join(mainStack)

sol = Solution()
# s = "(u(love)i)"
s = "(ed(et(oc))el)"
print(f'output: {sol.reverseParentheses(s)}')