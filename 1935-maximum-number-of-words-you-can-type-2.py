class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        '''
        Split the text into list of words, for each word, we check if any of the character of the word exists in the broken letters. If no, then add 1 to result
        '''
        result = 0
        words = text.split()

        for word in words:
            broken = False
            for c in word:
                if c in brokenLetters:
                    broken = True
                    break
            if not broken:
                result += 1

        return result


sol = Solution()
text = "hello world"
brokenLetters = "ad"
print(f'output: {sol.canBeTypedWords(text, brokenLetters)}, expected: 1')

text = "leet code"
brokenLetters = "lt"
print(f'output: {sol.canBeTypedWords(text, brokenLetters)}, expected: 1')

text = "leet code"
brokenLetters = "e"
print(f'output: {sol.canBeTypedWords(text, brokenLetters)}, expected: 0')
