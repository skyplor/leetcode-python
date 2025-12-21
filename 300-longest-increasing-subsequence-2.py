from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        we start from 1st element, it should have length of 1 so that is the base case
        then we proceed on to the next element and each time we compare against ALL previous nums. if this num is greater, then we take the calculated length for that index and add 1 to it.
        We then get the max between the current saved max length for this current element and the new length we calculated and store it in the dp
        At the end, we return the max of the dp
        Complexity: Time O(n^2), Space O(n)
        '''
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


sol = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
output = sol.lengthOfLIS(nums)
print(f'nums: {nums}\noutput: {output}')
