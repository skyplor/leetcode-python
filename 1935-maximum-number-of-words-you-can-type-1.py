class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        '''
        Split the text into list of words, for each word, we check if any of the broken letters exists in the word. If no, then add 1 to result
        '''
        result = 0
        words = text.split()
        broken_set = set(brokenLetters)

        for word in words:
            word_set = set(word)
            if len(word_set & broken_set) == 0:
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