from treenode import TreeNode
from typing import Optional

class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    '''
      loop through the nodes
      get the left node, invert the left node
      get the right node, invert the right node
    '''
    if not root: return None
    tmp = root.left
    root.left = root.right
    root.right = tmp

    self.invertTree(root.left)
    self.invertTree(root.right)
    
    return root
  
sol = Solution()
