from treenode import TreeNode, createBTree

class Solution:
  def goodNodes(self, root: TreeNode) -> int:
    '''
    res to store and increment
    dfs, each iteration, we have a curMax variable.
    compare current node value with curMax variable, if curMax <= current node, res += 1. curMax = max(curMax, node.val)
    move to the next
    '''
    res = 0
    def dfs(curMax, cur):
      nonlocal res

      if not cur:
        return
      if curMax <= cur.val:
        res += 1

      curMax = max(curMax, cur.val)
      dfs(curMax, cur.left)
      dfs(curMax, cur.right)

    dfs(float('-inf'), root)
    
    return res

sol = Solution()
# root = createBTree([3,1,4,3,None,1,5])
# root = createBTree([3,3,None,4,2])
root = createBTree([1])
print(f'output: {sol.goodNodes(root)}')
