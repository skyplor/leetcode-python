from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # mid is in the left sorted portion
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # mid is in the right sorted portion
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


sol = Solution()
# nums = [4,5,6,7,0,1,2]
# target = 0
nums = [4, 5, 6, 7, 0, 1, 2]
target = 1
output = sol.search(nums, target)
print(f'nums: {nums}\ntarget: {target}\noutput: {output}')
