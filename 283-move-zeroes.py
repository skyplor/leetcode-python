from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        2 pointers slow and fast. if fast is 0, continue. if slow value is 0, swap with fast then increment slow
        '''
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


sol = Solution()
# nums = [0, 1, 0, 3, 12]
nums = [1, 0, 1]
sol.moveZeroes(nums)
output = nums
print(f'output: {output}')
