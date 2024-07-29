from treenode import TreeNode, createBTree

class Solution:
  def countPairs(self, root: TreeNode, distance: int) -> int:
    '''
    Determine leaf nodes - no left and right children
    '''
    count = 0
    def dfs(node):
      nonlocal count
      if not node:
        return []
      if not node.left and not node.right:
        return [1]
      left = dfs(node.left)
      right = dfs(node.right)

      # for each node in the binary tree,
      # the function is counting the number of pairs of distances from its left and right subtrees that are within a specified distance.
      # The total count of such pairs is accumulated in the count variable.
      # for l in left:
      #   for r in right:
      #     count += (l+r <= distance)
      # short form:
      count += sum(l+r<=distance for l in left for r in right)

      # generates a new list by incrementing each element in the concatenated list left + right by 1
      # but only including those results that are less than distance.
      return [n + 1 for n in left + right if n + 1 < distance]
    
    dfs(root)
    return count
  
sol = Solution()
root = createBTree([1,2,3,None,4])
distance = 3
print(f'output: {sol.countPairs(root, distance)}')