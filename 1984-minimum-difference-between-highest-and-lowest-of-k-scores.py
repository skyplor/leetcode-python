class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        '''
        We first sort the nums so each group of k-elements are close to each other.
        This ensures that the difference between highest and lowest is closest if we choose the contiguous groups.
        Next, we just use sliding window and calculate the differences and get the min
        '''
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums) - k + 1):
            curr_diff = nums[i+k-1] - nums[i]
            if curr_diff < min_diff:
                min_diff = curr_diff

        return min_diff


sol = Solution()
print(f'output: {sol.minimumDifference(nums=[90], k=1)}, expected: 0')
print(f'output: {sol.minimumDifference(nums=[9, 4, 1, 7], k=2)}, expected: 2')
