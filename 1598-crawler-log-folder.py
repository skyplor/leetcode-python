from typing import List

class Solution:
  def minOperations(self, logs: List[str]) -> int:
    '''
    We can use a variable to (+1) each time we traverse to a child node and (-1) if we encounter '../'
    at the end, we just return that variable
    '''
    res = 0
    for item in logs:
      if item == '../':
        res = max(0, res - 1)
      elif item == './':
        continue
      else:
        res += 1
    return res

sol = Solution()
# logs = ["d1/","d2/","../","d21/","./"]
# logs = ["d1/","d2/","./","d3/","../","d31/"]
logs = ["d1/","../","../","../"]
print(f'output: {sol.minOperations(logs)}')