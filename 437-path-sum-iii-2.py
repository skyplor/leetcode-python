from treenode import TreeNode, deserialize, drawtree
from typing import Optional
from collections import defaultdict


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        To get the path sum up till a particular node from root, we would take the sum that we have calculated so far and add the current node's val. Then we store this sum in a dictionary
        Next, we go down the next node and repeat. At the same time, we want to also try to find if there exists a path along this path that we have calculated that contains the targetSum. 
            - How we do it is we can subtract the current sum by the targetSum, and find if we have previously found the difference.
            - If path_sums[current_sum - targetSum] exists,
                - it means there was a previous point in our path where the sum was current_sum - targetSum.
                - The subpath from that point to the current node has sum = current_sum - (current_sum - targetSum) = targetSum.
                - So we found a valid path!

            e.g
                Path: [10, 5, 3] with targetSum = 8
                - At 10: sum=10, store path_sums[10]=1, check path_sums[10-8=2] (no path found)
                - At 5: sum=15, store path_sums[15]=1, check path_sums[15-8=7] (no path found)
                - At 3: sum=18, store path_sums[18]=1, check path_sums[18-8=10]
                - Found path_sums[10]=1, so path [5→3] sums to 8!

                The nodes we "ignore" (node 10) plus the remaining nodes (5→3) together form the complete path, but only the remaining nodes (5→3) actually sum to our target.

        We will also need to make use of backtracking so that after we finish with the recursion to go down the children, we remove this pathSum that we have found

        So we will need a few variables to hold these data:
            - a dict of all pathSums found so far. The dict will have the pathSum as the key and the occurrence as the value. (So each time we go down a path and we found the same pathSum, we will add 1 to it. And each time we backtrack, we minus 1 from it)
                - We need to make sure to set a 1 to the key 0 in path_sums
            - a res variable that holds the total number of paths found for this targetSum. We can use an array so that the inner function can access and update it similar to a global var
        '''
        path_sums = defaultdict(int)
        res = [0]
        path_sums[0] = 1  # Base case: sum = 0 has one count

        def dfs(node: Optional[TreeNode], cur_sum: int):
            if not node:
                return

            new_sum = cur_sum + node.val
            res[0] += path_sums[new_sum - targetSum]

            path_sums[new_sum] += 1

            dfs(node.left, new_sum)
            dfs(node.right, new_sum)

            path_sums[new_sum] -= 1

        dfs(root, 0)
        return res[0]


sol = Solution()
# root = deserialize("[1,null,2,null,3,null,4,null,5]")
# targetSum = 3
# root = deserialize("[10,5,-3,3,2,null,11,3,-2,null,1]")
# targetSum = 8
root = deserialize("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
targetSum = 22
output = sol.pathSum(root, targetSum)
print(f'output: {output}')
