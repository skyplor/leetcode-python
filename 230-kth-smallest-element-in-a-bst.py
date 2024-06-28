from typing import Optional
from treenode import TreeNode, createBTree
from heapq import heappop, heappush

class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    '''
    we can do in-order traversal of BST and each time we increment n and once n == k, we can return the last element in that list
    we can use a stack to do in-order traversal of BST
    '''
    n = 0
    stack = []
    cur = root
    while cur or stack:
      while cur:
        stack.append(cur)
        cur = cur.left

      cur = stack.pop()
      n += 1
      if n == k:
        return cur.val
      cur = cur.right

    return -1
      

sol = Solution()
root = createBTree([3,1,4,None,2])
k = 2
# root = createBTree([5,3,6,2,4,None,None,1])
# k = 3
print(f'output: {sol.kthSmallest(root, k)}')