from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)
        vowel_set = set(['a', 'e', 'i', 'o', 'u'])
        max_vowel = 0
        max_consonent = 0
        for k, v in count.items():
            if k in vowel_set:
                max_vowel = max(max_vowel, v)
            else:
                max_consonent = max(max_consonent, v)
                
        return max_vowel + max_consonent


sol = Solution()
s = "successes"
print(f'output: {sol.maxFreqSum(s)}, expected: 6')
s = "aeiaeia"
print(f'output: {sol.maxFreqSum(s)}, expected: 3')
