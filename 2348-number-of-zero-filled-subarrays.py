from typing import List
from collections import defaultdict


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        '''
        We can make use of a hashmap to store how many consecutive 0s and then we calculate the number of permutations
        0: 1
        00: 2 + 1
        000: 3 + 2 + 1
        0000: 4 + 3 + 2 + 1
        00000: 5 + 4 + 3 + 2 + 1
        '''
        consecutive_zeros_map = defaultdict(int)
        current_zeros = 0
        for n in nums:
            if n == 0:
                current_zeros += 1
            else:
                if current_zeros:
                    consecutive_zeros_map[current_zeros] += 1
                    current_zeros = 0

        res = 0
        permutation_count = {}
        for key, value in consecutive_zeros_map.items():
            if key in permutation_count:
                multiplier = permutation_count[key]
            else:
                multiplier = 1
                for i in range(n, 0, -1):
                    multiplier += i

                permutation_count[key] = multiplier

            res += value * multiplier

        return res


sol = Solution()
nums = [1, 3, 0, 0, 2, 0, 0, 4]
print(f'output: {sol.zeroFilledSubarray(nums)}')
