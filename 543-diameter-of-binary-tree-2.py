from treenode import TreeNode, createBTree
from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        We traverse the tree using DFS (recursion)
        we get the current diameter of the node to be (left + right)
        then we update res if this is larger
        we then return the height of this branch to the parent (max(left, right) + 1)
        at the end, we return the result
        '''
        res = [0]
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res[0] = max(res[0], left + right)
            return max(left, right) + 1
        dfs(root)
        return res[0]

sol = Solution()
root = createBTree([1,2,3,4,5])
output = sol.diameterOfBinaryTree(root)
print(f'output: {output}')
