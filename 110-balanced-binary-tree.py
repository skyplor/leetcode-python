from treenode import TreeNode, createBTree, drawtree
from typing import Optional

class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    '''
      we store the isBalanced result for each node
    '''
    def dfs(root):
      if not root:
        return [True, 0]
      left_balanced, left_height = dfs(root.left)
      right_balanced, right_height = dfs(root.right)
      children_balanced = left_balanced and right_balanced
      current_balanced = abs(left_height - right_height) <= 1

      return [children_balanced and current_balanced, 1 + max(left_height, right_height)]
      
    return dfs(root)[0]
  
sol = Solution()
# input = [3,9,20,None,None,15,7]
# input = [3,9,20,8,4,15,7]
input = [1,2,2,3,3,None,None,4,4]
root = createBTree(input, 0)
output = sol.isBalanced(root)
print(f'input: {input}\noutput: {output}')
print(f'input: {input}\noutput: {drawtree(root)}')