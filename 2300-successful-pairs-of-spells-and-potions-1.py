import math

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        '''
        len (result) = len(spells)
        We can sort the potions in ascending order and do binary search for the index with a value that is equal or bigger than (`success` + 1 // spells[i])
        '''
        n, m = len(spells), len(potions)
        result = [0] * n
        potions.sort()

        def binary_search(left, right, target):
            while left < right:
                mid = left + (right - left) // 2
                if potions[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        for i in range(n):
            spell = spells[i]
            idx = binary_search(0, m, math.ceil(success / spell))
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
