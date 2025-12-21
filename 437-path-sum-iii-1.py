from treenode import TreeNode, createBTree, drawtree
from typing import List, Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        Brute force method where we go through each node and from each node go down the path.
        Time: O(n^2)
        Space: O(n) (worse case complexity for skewed tree. If it's a balanced tree, then it would be O(log n))
        '''

        def dfs(current_node, current_target_sum):
            if not current_node:
                return 0

            count = 0
            new_target_sum = current_target_sum - current_node.val
            if new_target_sum == 0:
                count += 1

            count += dfs(current_node.left, new_target_sum)
            count += dfs(current_node.right, new_target_sum)

            return count
        if not root:
            return 0

        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)


sol = Solution()
root = createBTree([1, None, 2, None, 3, None, 4, None, 5])
targetSum = 3
# root = createBTree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
# targetSum = 8
# root = createBTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
# targetSum = 22
output = sol.pathSum(root, targetSum)
print(f'output: {output}')
