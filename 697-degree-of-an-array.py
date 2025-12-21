from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        num_occurrence = {}
        for i, n in enumerate(nums):
            freq[n] = freq.get(n, 0) + 1
            if n not in num_occurrence:
                num_occurrence[n] = [i, i]
            else:
                num_occurrence[n][1] = i

        max_count = 0

        min_length = float('inf')
        max_count = max(freq.values())

        for num, count in freq.items():
            if count == max_count:
                start, end = num_occurrence[num]
                length = end - start + 1
                min_length = min(min_length, length)

        return min_length
    
sol = Solution()
nums = [1,2,2,3,1,4,2]
output = sol.findShortestSubArray(nums)
print(f'output: {output}')