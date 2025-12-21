from collections import defaultdict


class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        '''
        We can use a modified of prefix sum and suffix sum whereby we calculate for each number at j,
        how many occurrences of number * 2 are there before it (prefix sum)

        Next, we loop through again but from the back and do the same check and multiply the 2 values at each index and sum them up
        '''
        MOD = 10 ** 9 + 7
        n = len(nums)
        prefix = [0] * n
        count = defaultdict(int)
        for j, num in enumerate(nums):
            prefix[j] = count[num * 2]
            count[num] += 1

        res = 0
        count = defaultdict(int)
        for j in range(n - 1, -1, -1):
            num = nums[j]
            suffix = count[num * 2]
            res = (res + (prefix[j] * suffix)) % MOD
            count[num] += 1

        return res


sol = Solution()
print(f'output: {sol.specialTriplets([6, 3, 6])}, expected: 1')
print(f'output: {sol.specialTriplets([0, 1, 0, 0])}, expected: 1')
print(f'output: {sol.specialTriplets([8, 4, 2, 8, 4])}, expected: 2')
print(f'output: {sol.specialTriplets([8, 4, 8, 4, 8])}, expected: 4')
