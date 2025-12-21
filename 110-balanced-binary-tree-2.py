from treenode import TreeNode, createBTree, drawtree
from typing import Optional, Union


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
          we store the isBalanced result for each node
        '''
        def isSubBalanced(node: Optional[TreeNode]) -> Union[int, bool]:
            if not node:
                return 0, True
            left_level, left_balanced = isSubBalanced(node.left)
            right_level, right_balanced = isSubBalanced(node.right)
            return (max(left_level, right_level) + 1, left_balanced and right_balanced and abs(left_level - right_level) <= 1)

        return isSubBalanced(root)[0]


sol = Solution()
# input = [3,9,20,None,None,15,7]
# input = [3,9,20,8,4,15,7]
input = [1, 2, 2, 3, 3, None, None, 4, 4]
root = createBTree(input, 0)
output = sol.isBalanced(root)
print(f'input: {input}\noutput: {output}')
print(f'input: {input}\noutput: {drawtree(root)}')
