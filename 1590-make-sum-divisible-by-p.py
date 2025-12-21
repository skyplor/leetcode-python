class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        '''
        We can do the opposite, sum up the entire list, get the remainder after divided by `p`. Let's name it `k`
        Then we find the smallest subarray that sums up and divided by `p` with remainder equals to the above remainder
        At each index, we get the prefix sum.
        Next, we can get the subarray sum from `j+1` to `i` using prefix_sum[i] - prefix_sum[j] and if we get the remainder after dividing by p, we want that to be equal to `k`
        We keep track of all the prefix sums in a hashmap with value being the index
        Next, we go through each index `i`, if (pref[i] - k) % p appeared before in the hashmap, we get the index value and that is j. the length will be (i - j)
        '''
        total = sum(nums)
        if total < p:
            return -1
        k = total % p
        if k == 0:
            return 0
        n = len(nums)
        hash = {0: -1}
        res = n
        curr_total = 0
        for i, num in enumerate(nums):
            curr_total = (curr_total + num) % p
            target = (curr_total - k + p) % p

            if target in hash:
                res = min(res, i - hash[target])

            hash[curr_total] = i

        return -1 if res == n else res


sol = Solution()
print(f'output: {sol.minSubarray(nums=[3, 1, 4, 2], p=6)}, expected: 1')
print(f'output: {sol.minSubarray(nums=[6, 3, 5, 2], p=9)}, expected: 2')
print(f'output: {sol.minSubarray(nums=[1, 2, 3], p=3)}, expected: 0')
