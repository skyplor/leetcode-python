from treenode import TreeNode, createBTree, drawtree
from typing import List, Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def get_path(current_node, path, target_sum):
            if not current_node:
                return

            path.append(current_node.val)
            new_target_sum = target_sum - current_node.val

            if not current_node.left and not current_node.right and new_target_sum == 0:
                res.append(path)

            get_path(current_node.left, path.copy(), new_target_sum)
            get_path(current_node.right, path.copy(), new_target_sum)

        get_path(root, [], targetSum)
        return res


sol = Solution()
root = createBTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
targetSum = 22
output = sol.pathSum(root, targetSum)
print(f'output: {output}')
