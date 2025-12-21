import math
import bisect


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        '''
        len (result) = len(spells)
        We can sort the potions in ascending order and do binary search for the index with a value that is equal or bigger than (`success` + 1 // spells[i])
        '''
        n, m = len(spells), len(potions)
        result = [0] * n
        potions.sort()

        for i in range(n):
            spell = spells[i]
            # For bisect_left, this is when we want to find the index >= target (i.e. the first index where the value is equal to or larger than the target)
            # For bisect_right, that means we want to find the first index where the value is larger than the target
            #   e.g [1, 2, 2, 2, 5] with target 2
            #       bisect_left returns index 1
            #       bisect_right returns index 4
            #
            # For this case, since we want to find the index >= target, we use bisect_left
            idx = bisect.bisect_left(potions, math.ceil(success / spell))
            result[i] = max(0, m - idx)

        return result


sol = Solution()
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(
    f'output: {sol.successfulPairs(spells, potions, success)}, expected: {[4, 0, 3]}')
spells = [3, 1, 2]
potions = [8, 5, 8]
success = 16
print(
    f'output: {sol.successfulPairs(spells, potions, success)}, expected: {[2, 0, 2]}')
