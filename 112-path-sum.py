from treenode import TreeNode, createBTree
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        We use DFS to recursively go down each node, each time reducing the target sum based on the current node's value.
        Once we found a leaf node, we will need to check that the target sum is 0 and if yes, we return as True
        '''
        if not root:
            return False

        new_target_sum = targetSum - root.val
        if not root.left and not root.right and new_target_sum == 0:
            return True
        return self.hasPathSum(root.left, new_target_sum) or self.hasPathSum(root.right, new_target_sum)


sol = Solution()
root = createBTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
targetSum = 22
output = sol.hasPathSum(root, targetSum)
print(f'output: {output}')
