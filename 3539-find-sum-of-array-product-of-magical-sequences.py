from functools import lru_cache
import math


class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        '''
        
        '''
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(remaining, odd_needed, index, carry):
            if remaining < 0 or odd_needed < 0 or remaining + carry.bit_count() < odd_needed:
                return 0
            if remaining == 0:
                return 1 if odd_needed == carry.bit_count() else 0
            if index >= len(nums):
                return 0
            
            ans = 0
            for take in range(remaining + 1):
                ways = math.comb(remaining, take) * pow(nums[index], take, MOD) % MOD
                new_carry = carry + take
                ans += ways * dfs(remaining - take, odd_needed - (new_carry % 2), index + 1, new_carry // 2)
                ans %= MOD
            return ans
        
        return dfs(m, k, 0, 0)


sol = Solution()
m = 5
k = 5
nums = [1, 10, 100, 10000, 1000000]
print(f'output: {sol.magicalSum(m, k, nums)}, expected: 991600007')
m = 2
k = 2
nums = [5, 4, 3, 2, 1]
print(f'output: {sol.magicalSum(m, k, nums)}, expected: 170')
m = 1
k = 1
nums = [28]
print(f'output: {sol.magicalSum(m, k, nums)}, expected: 28')
