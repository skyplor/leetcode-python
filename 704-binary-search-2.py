class Solution:
    def binarySearch(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return -1


sol = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
output = sol.binarySearch(nums, target)
print(f'nums: {nums}\ntarget: {target}\noutput: {output}')
