from treenode import TreeNode
from typing import Optional

class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    '''
      We use DFS and add the left and right depths
    '''
    res = 0
    def dfs(node):
      nonlocal res

      if not node:
        return 0
      left = dfs(node.left)
      right = dfs(node.right)
      res = max(res, left + right)

      return 1 + max(left, right)

    dfs(root)
    return res
  
sol = Solution()