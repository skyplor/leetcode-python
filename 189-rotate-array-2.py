from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        '''
        We reverse the entire array first
        Then we reverse the first k elements
        Then we reverse the remaining elements
        '''
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)


sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(f'output: {sol.rotate(nums, k)}')
