class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        '''
        We choose a starting point that is at 0, then get the sum of all numbers to the left of it and the sum of all numbers to the right of it. If it equals, we have a solution. Else, we don't
        '''
        zero_indices = []
        for i, num in enumerate(nums):
            if num == 0:
                zero_indices.append(i)
                
        res = 0
        for idx in zero_indices:
            left = sum(nums[:idx])
            right = sum(nums[idx+1:])
            if left == right:
                res += 2
            if abs(left - right) == 1:
                res += 1
                
        return res


sol = Solution()
print(f'output: {sol.countValidSelections([1, 0, 2, 0, 3])}, expected: 2')
print(
    f'output: {sol.countValidSelections([2, 3, 4, 0, 4, 1, 0])}, expected: 0')
