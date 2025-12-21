from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Using recursion, each time we will extract out the nums from position 1 to n-1, pass it into the recursive function
        Then, we have a loop that will loop through each permutation of the nums (1 to n - 1) returned. We will then insert the nums[0] into each position
        Take note that the loop will loop to len(perms) + 1 as we are inserting an additional number
        Also take note that we need to make a copy of the perms before inserting so that we can reuse that perms for other loops
        After inserting, we then append into the result list
        The base case is if the nums is an empty array
        '''
        if not nums:
            return [[]]

        res = []
        perms = self.permute(nums[1:])

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res


sol = Solution()
nums = [1, 2, 3]
output = sol.permute(nums)
print(f'nums: {nums}\noutput: {output}')
