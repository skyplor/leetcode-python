class Solution:
    def doesAliceWin(self, s: str) -> bool:
        '''
        We can count the number of vowels to determine the winner.
        0 vowels, Bob wins
        1 vowel, Alice wins
        2 vowels, Alice wins (Alice remove 1 vowel, Bob remove 0 vowels, Alice remove 1 vowel, Alice wins)
        3 vowels, Alice wins (Alice remove 3 vowels, Alice wins)
        ...
        So as long as more than 0 vowels, Alice wins. Else Bob wins
        '''
        VOWELS = 'aeiou'
        for c in s:
            if c in VOWELS:
                return True

        return False


sol = Solution()
s = "leetcoder"
print(f'output: {sol.doesAliceWin(s)}, expected: True')
s = "bbcd"
print(f'output: {sol.doesAliceWin(s)}, expected: False')
