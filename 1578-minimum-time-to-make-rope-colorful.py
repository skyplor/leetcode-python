from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        '''
        We go through each color and compare with the next color. If both are the same, we get take the one that has smaller neededTime and add it into our result
        '''
        if len(colors) == 1:
            return 0
        result = 0
        prev_idx = 0
        
        for i in range(1, len(colors)):
            if colors[prev_idx] == colors[i]:
                if neededTime[i] < neededTime[prev_idx]:
                    result += neededTime[i]
                else:
                    result += neededTime[prev_idx]
                    prev_idx = i
                    
            else:
                prev_idx = i

        return result


sol = Solution()
colors = "abaac"
neededTime = [1, 2, 3, 4, 5]
print(f'output: {sol.minCost(colors, neededTime)}, expected: 3')
colors = "abc"
neededTime = [1, 2, 3]
print(f'output: {sol.minCost(colors, neededTime)}, expected: 0')
colors = "aabaa"
neededTime = [1, 2, 3, 4, 1]
print(f'output: {sol.minCost(colors, neededTime)}, expected: 2')
colors = "aaabbbabbbb"
neededTime = [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]
print(f'output: {sol.minCost(colors, neededTime)}, expected: 26')
