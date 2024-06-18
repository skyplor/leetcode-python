from treenode import TreeNode, createBTree,drawtree
from typing import Optional, List
from collections import deque

class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []

    res = []
    queue = deque()
    queue.append(root)
    while queue:
      current_nodes = []
      for _ in range(len(queue)):      
        current = queue.popleft()

        current_nodes.append(current.val)

        if current.left:
          queue.append(current.left)
        if current.right:
          queue.append(current.right)

      res.append(current_nodes)
      
    return res
  
sol = Solution()
# root = createBTree([3,9,20,None,None,15,7], 0)
root = createBTree([1,2,3,4,None,None,5], 0)
# print(drawtree(root))
output = sol.levelOrder(root)
print(f'root: {root}\noutput: {output}')