from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        We have a res list in the main function.
        Using backtracking, we have 2 arguments (current list and the index)
        The base case is if the index == length of nums, we add current into the list
        We get the current num to process using the index. Then we have 2 scenarios. Either we include that num or don't include that num (and simply just increment index)
        So we call backtracking twice. To include the num, we need to copy the current list, and append the num. Otherwise, we just pass in the current
        '''
        res = []

        def backtracking(current: List[int], i: int):
            if i >= len(nums):
                res.append(current)
                return

            # include this num
            backtracking(current + [nums[i]], i+1)

            # don't include this num
            backtracking(current, i+1)

        backtracking([], 0)
        return res


sol = Solution()
nums = [1, 2, 3]
output = sol.subsets(nums)
print(f'nums: {nums}\noutput: {output}')
