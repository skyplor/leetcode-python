class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        iterate using a counter with max value as the longest length
        on each iteration, check if the counter is larger than the length of the word1. If not, append into the res
        do the same for word2
        '''
        res = []
        word1_len = len(word1)
        word2_len = len(word2)
        max_length = max(word1_len, word2_len)
        for i in range(max_length):
            if i < word1_len:
                res.append(word1[i])
            if i < word2_len:
                res.append(word2[i])

        return ''.join(res)


sol = Solution()
word1 = 'ab'
word2 = 'pqrs'
output = sol.mergeAlternately(word1, word2)
print(f'output: {output}')
