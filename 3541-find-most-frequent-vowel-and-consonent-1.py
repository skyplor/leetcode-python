class Solution:
    def maxFreqSum(self, s: str) -> int:
        '''
        Create an array of size 26 to house the count of the 26 characters. We then pick the max out of the 'a, e, i, o, u', and the max out of the remaining
        '''
        count = [0] * 26
        max_vowel = 0
        max_consonent = 0
        for c in s:
            index = ord(c) - ord('a')
            count[index] += 1
            if c in 'aeiou':
                max_vowel = max(max_vowel, count[index])
            else:
                max_consonent = max(max_consonent, count[index])
        
        return max_vowel + max_consonent


sol = Solution()
s = "successes"
print(f'output: {sol.maxFreqSum(s)}, expected: 6')
s = "aeiaeia"
print(f'output: {sol.maxFreqSum(s)}, expected: 3')
