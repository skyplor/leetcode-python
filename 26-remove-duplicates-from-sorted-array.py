from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        2 pointers, slow and fast. Slow will be the pointer that will only move by 1 when fast finds the next unique value.
        slow starts at index 0, fast starts at index 1
        if nums[fast] != nums[slow], slow += 1, copies nums[slow] = nums[fast]
        '''

        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


sol = Solution()
nums = [1, 1, 2]
output = sol.removeDuplicates(nums)
print(f'output: {output}')
