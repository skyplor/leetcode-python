from typing import Optional, List
from treenode import TreeNode, drawtree

class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # preorder = cur, left, right
    # inorder = left, cur, right
    '''
    first value in preorder is the root
    remove that node, search for that node in inorder list
    anything to the left of the node in the inorder list will belong to the left of the tree,
    anything to the right of the node in the inorder list will belong to the right of the tree
    so we can get the length of each left and right, then we iterate preorder list to partition into left and right
    and we do this recursively
    '''
    def dfs(preorder, inorder):
      if not preorder or not inorder:
        return None
      root = TreeNode(preorder[0])
      mid = inorder.index(root.val)
      root.left = dfs(preorder[1:mid + 1], inorder[:mid])
      root.right = dfs(preorder[mid + 1:], inorder[mid+1:])
      return root
      
    return dfs(preorder, inorder)
  
sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
drawtree(sol.buildTree(preorder, inorder))