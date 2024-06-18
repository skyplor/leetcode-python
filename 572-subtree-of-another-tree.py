from treenode import TreeNode, createBTree
from typing import Optional

class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root or not subRoot: return False

    def isSame(p, q):
      queue1, queue2 = [p], [q]
      while queue1 and queue2:
        node1, node2 = queue1.pop(), queue2.pop()
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
    
    queue = [root]

    while queue:
      node = queue.pop()
      if not node:
        continue
      if node.val == subRoot.val:
        if isSame(node, subRoot):
          return True
      queue.append(node.left)
      queue.append(node.right)
        
    return False
  
sol = Solution()
root = createBTree([3,4,5,1,2], 0)
subRoot = createBTree([4,1,2], 0)
output = sol.isSubtree(root, subRoot)
print(f'root: {root}\nsubRoot: {subRoot}\noutput: {output}')