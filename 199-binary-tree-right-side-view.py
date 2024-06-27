from typing import List, Optional
from treenode import TreeNode, createBTree
from collections import deque

class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root: return []
    res = []
    queue = deque([root])
    while queue:
      curLevel = deque()
      curLevelNode = None
      for _ in range(len(queue)):
        curLevel.append(queue.popleft())
      while curLevel:
        node = curLevel.popleft()
        curLevelNode = node
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)

      if curLevelNode:
        res.append(curLevelNode.val)
      
    return res
  
sol = Solution()
# root = createBTree([1,2,3,None,5,None,4])
# root = createBTree([1,2])
root = createBTree([1,2,3,4])
print(f'output: {sol.rightSideView(root)}')