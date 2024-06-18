from typing import Optional
from treenode import TreeNode, createBTree

class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    queue1, queue2 = [p], [q]

    while queue1 and queue2:
      node1 = queue1.pop()
      node2 = queue2.pop()
      if not node1 and not node2:
        continue
      if node1 and node2:
        if node1.val != node2.val:
          return False
        queue1.append(node1.left)
        queue1.append(node1.right)
        queue2.append(node2.left)
        queue2.append(node2.right)
      else:
        return False
      
    return not (queue1 and queue2)
  
sol = Solution()
# p = createBTree([1,2,3], 0)
# q = createBTree([1,2,3], 0)
p = createBTree([1,2], 0)
q = createBTree([1,None,2], 0)
output = sol.isSameTree(p, q)
print(f'p: {p}\nq: {q}\noutput: {output}')