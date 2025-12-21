class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        '''
        We first get the total sum of the nums
        We go through each index,
            - at each `i`,
                - We can have a cur_total var that calculates the total up till this `i` index
                - then we calculate the sum of right subarray by subtracting `cur_total` from `total`
                - next, we calculate the difference between these 2 and if it's even, we add 1 to the `res` count

        '''
        total = sum(nums)
        cur_total = 0
        res = 0
        for i in range(0, len(nums) - 1):
            cur_total += nums[i]
            right_total = total - cur_total
            if (cur_total - right_total) % 2 == 0:
                res += 1

        return res


sol = Solution()
print(f'output: {sol.countPartitions([10, 10, 3, 7, 6])}, expected: 4')
print(f'output: {sol.countPartitions([1, 2, 2])}, expected: 0')
print(f'output: {sol.countPartitions([2, 4, 6, 8])}, expected: 3')
