class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        '''
        This is an extension of binary search.
        Instead of checking if the mid is == target, and returning the mid if it does, we need to check if mid is greater than or equal to target, and to also check if the element before the mid is smaller than target
        We also need to consider the case if mid is the first element. Then we can just return that index
        Lastly, if we can't find any, that means this target will be appended to the array, so we return the length of the nums
        '''
        left = 0
        right = len(nums)
        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] >= target and (mid == 0 or nums[mid - 1] < target):
                return mid
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1

        return len(nums)


sol = Solution()
nums = [1, 3, 5, 6]
# target = 5
# nums = [1,3,5,6]
# target = 2
# nums = [1,3,5,6]
target = 7
output = sol.searchInsert(nums, target)
print(f'output: {output}')
