from treenode import TreeNode, createBTree
from typing import Optional

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    '''
      if p < current node and q > current node, then we know current node is the lowest common ancestor
      because it is where the split happens
      if p == current node and q > or < current node, then p is the LCA, vice versa
    '''
    current = root
    while current:
      if (p.val > current.val and q.val < current.val) or (p.val < current.val and q.val > current.val):
        return current
      if p.val == current.val or q.val == current.val:
        return current
      if p.val > current.val:
        current = current.right
      else:
        current = current.left
        
    return root
  
sol = Solution()
# root = createBTree([6,2,8,0,4,7,9,None,None,3,5], 0)
# p = root.left
# q = root.left.right
root = createBTree([6,2,8,0,4,7,9,None,None,3,5], 0)
p = root.left
q = root.right.left
output = sol.lowestCommonAncestor(root, p, q)
print(f'root: {root}\np: {p}\nq: {q}\noutput: {output}')
