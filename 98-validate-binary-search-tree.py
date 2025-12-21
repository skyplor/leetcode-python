from treenode import TreeNode, createBTree, drawtree
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        We can use recursion to check if the left and right children are valid BST and left < cur and right > cur and if so we can return true
        base case is if root is None, we can return True
        we need to pass down the min and max value
        '''

        def isValidSubBST(node: Optional[TreeNode], min: int, max: int) -> bool:
            if not node:
                return True

            left_valid = right_valid = True

            if node.left:
                left_valid_bst = isValidSubBST(node.left, min, node.val)
                left_valid = left_valid_bst and node.left.val > min and node.left.val < node.val

            if node.right:
                right_valid_bst = isValidSubBST(node.right, node.val, max)
                right_valid = right_valid_bst and node.right.val > node.val and node.right.val < max

            return left_valid and right_valid

        return isValidSubBST(root, float('-inf'), float('inf'))


sol = Solution()
# root = createBTree([2, 1, 3])
# root = createBTree([5, 1, 4, None, None, 3, 6])
root = createBTree([5, 4, 6, None, None, 3, 7])
# root = createBTree([24,-60,None,-60,-6])
# drawtree(root)
output = sol.isValidBST(root)
print(f'output: {output}')
