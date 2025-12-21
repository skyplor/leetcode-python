class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        iterate using word1, append the word1 character into res
        try to retrieve from word2. if unable, exit the loop
        depending on which is the longer str, we get the length and get the difference of the length and append from the difference to end of the longer str
        '''
        res = []
        for idx, c in enumerate(word1):
            res.append(c)
            if len(word2) - 1 >= idx:
                res.append(word2[idx])

        if len(word1) == len(word2):
            return ''.join(res)

        longerStr = word1
        startingIndex = len(word1)
        if len(word2) > len(word1):
            longerStr = word2
            startingIndex = len(word1)

        res.append(longerStr[startingIndex:])

        return ''.join(res)


sol = Solution()
word1 = 'ab'
word2 = 'pqrs'
output = sol.mergeAlternately(word1, word2)
print(f'output: {output}')
