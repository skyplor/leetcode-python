class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        '''
        This is an extension of binary search.
        Instead of checking if the mid is == target, and returning the mid, we will just check for more than or equal and less than and moving the right pointer or left pointer respectively
        At the end, we just return the left pointer
        '''
        left = 0
        right = len(nums)
        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left


sol = Solution()
nums = [1, 3, 5, 6]
# target = 5
# nums = [1,3,5,6]
# target = 2
# nums = [1,3,5,6]
target = 7
output = sol.searchInsert(nums, target)
print(f'output: {output}')
