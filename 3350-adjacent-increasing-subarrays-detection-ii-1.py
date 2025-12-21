import math

class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        '''
        We have a max_k var and each time we have a match, we increment the count, making use of binary search
        '''

        def binary_search(start, end):
            while start <= end:
                k = start + (end - start) // 2
                valid_k = hasIncreasingSubarrayOfLengthK(k)
                if valid_k:
                    start = k + 1
                else:
                    end = k - 1
            return end

        def hasIncreasingSubarrayOfLengthK(k):
            first, second = 1, k+1
            count = 0
            if k == 1:
                return len(nums) >= 2

            while second < len(nums):
                if nums[first - 1] < nums[first] and nums[second - 1] < nums[second]:
                    count += 1
                    if count == k - 1:
                        return True
                else:
                    count = 0

                first += 1
                second += 1

            return False

        max_k = binary_search(1, math.ceil(len(nums) / 2))

        return max_k


sol = Solution()
print(
    f'output: {sol.maxIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1])}, expected: 3')
print(
    f'output: {sol.maxIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7])}, expected: 2')
print(
    f'output: {sol.maxIncreasingSubarrays([-15, 9])}, expected: 1')
print(
    f'output: {sol.maxIncreasingSubarrays([5, 8, -2, -1])}, expected: 2')
