from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        e.g 
        [2 7 9 3 1]
            2 -> 9 -> 1
            2 -> 3
            2 -> 1
            7 -> 3
            9 -> 1
        
        Treating each num as a node, and this entire problem as a DAG (directed acyclic graph)
        we can get the max amount by checking for max at n-2 + value of n and max at n-1
        then we get the max amount out of those 2
        base case:
            n == 1: return nums[n]
            n == 2: return max(nums[1], nums[2])
            
        we also need memo
        '''

        memo = {}
        n = len(nums)
        if n < 2:
            return nums[0]

        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            if i in memo:
                return memo[i]
            memo[i] = max(memo[i - 2] + nums[i], memo[i - 1])
            
        return memo[n-1]
        

sol = Solution()
nums = [1,2,3,1]
# nums = [2, 1, 1, 2]
print(f'nums: {nums}')
output = sol.rob(nums)

print(f'output: {output}')
