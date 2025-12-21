from collections import defaultdict


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        '''
        We will do this in 2-pass.
        First pass, we use a hash/dict to store the count of all the numbers
        Next, we find the max from the dict's values
        Lastly, we go through the dict and if a number has the maximum value, we add the max_value to result
        '''
        result = 0
        hash = defaultdict(int)
        for num in nums:
            hash[num] += 1

        max_count = max(hash.values())

        for value in hash.values():
            if value == max_count:
                result += max_count

        return result


sol = Solution()
nums = [1, 2, 2, 3, 1, 4]
print(f'output: {sol.maxFrequencyElements(nums)}, expected: 4')
nums = [1, 2, 3, 4, 5]
print(f'output: {sol.maxFrequencyElements(nums)}, expected: 5')
