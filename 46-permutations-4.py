from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        we define a backtracking function that accepts a current list. 
        Base case: if this current list has ALL the nums, then we append this current into the result list
        
        Otherwise, we go through each num in the nums, for each iteration,
        if this num is not in the list, we will need to add it in.
        We copy the current list, append the num, then calls backtracking with this new copy
        
        '''
        
        res = []
        def backtracking(current: List[int]):
            if len(current) == len(nums):
                res.append(current)
                return
            
            for num in nums:
                if num in current:
                    continue
                
                c_copy = current.copy()
                c_copy.append(num)
                backtracking(c_copy)

        backtracking([])
        return res


sol = Solution()
nums = [1, 2, 3]
output = sol.permute(nums)
print(f'nums: {nums}\noutput: {output}')
