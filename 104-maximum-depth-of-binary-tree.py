from treenode import TreeNode
from typing import Optional

class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    def maxSubdepth(node, current_depth):
      if not node:
        return current_depth + 1
      
      left_depth = maxSubdepth(node.left, current_depth) if node.left else 0
      right_depth = maxSubdepth(node.right, current_depth) if node.right else 0
      current_depth += max(left_depth, right_depth)
      
      return current_depth
      
    return maxSubdepth(root, 0)
  
sol = Solution()