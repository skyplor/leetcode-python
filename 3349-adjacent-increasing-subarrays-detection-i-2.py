class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        '''
        We have 2 pointers that represent the starting.
        For each starting position, we move the pointer k times to check if it's strictly increasing.
            - If our counter == k, return True
            - Else, we reset the count and increment both pointers by 1
        '''
        start_first, start_second = 1, k + 1
        n = len(nums)
        count = 0
        if k == 1:
            return n >= 2

        while start_second < n:
            if nums[start_first - 1] < nums[start_first] and nums[start_second - 1] < nums[start_second]:
                count += 1
                if count == k - 1:
                    return True
            else:
                count = 0

            start_first += 1
            start_second += 1

        return False


sol = Solution()
print(
    f'output: {sol.hasIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3)}, expected: True')
print(
    f'output: {sol.hasIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5)}, expected: False')
print(f'output: {sol.hasIncreasingSubarrays([-15, 19], 1)}, expected: True')
print(
    f'output: {sol.hasIncreasingSubarrays([5, 8, -2, -1], 2)}, expected: True')
