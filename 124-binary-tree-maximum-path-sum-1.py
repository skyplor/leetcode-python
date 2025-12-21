from treenode import TreeNode, createBTree
from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        A path can only happen when there's at most 1 split happening for the entire path and it will be the start of the path.
        A split means to take the value of both left and right children.

        For example, for the following case, we can't take 2 + 1 + 3 + 5 + 4 (both 2 & 3 and both 5 & 4). 

        Valid scenarios:
        Scenario 1: 2 + 1 + 3 + 4 (2 & 3)
        Scenario 2: 2 + 1 + 3 + 5 (2 & 3)
        Scenario 3: 5 + 3 + 4 (5 & 4)
                1
               / \
              2   3
                 / \
                5   4

        The main logic behind this is that for each node, we will need to keep track / calculate what is the maximum sum we can get IF we split vs if we did not split.
        We can further break this problem into sub-problem by calculating the split and non-split scenarios for each children. 
        We will have a result variable that keep track of the maximum sum we have calculated so far. 
        Next, for split scenarios, once we calculate that, we can then check the result variable and update it if this value is greater. (Scenario 3)
        For non-spit scenarios, we pass this information back to the parent for further calculation (Scenarios 1 & 2)
        Lastly, we also need to consider cases if the value is negative. We will need to return 0 if it's negative to instead not consider that node
        '''
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            left_max = max(0, dfs(root.left))
            right_max = max(0, dfs(root.right))

            split_sum = left_max + root.val + right_max
            res[0] = max(res[0], split_sum)

            return max(left_max, right_max) + root.val
        dfs(root)
        return res[0]


sol = Solution()
root = createBTree([-10, 9, 20, None, None, 15, 7])
output = sol.maxPathSum(root)
print(f'output: {output}')
