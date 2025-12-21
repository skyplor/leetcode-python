class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        '''
        We also have 2 lists of characters, `left` and `right` of length 26 (representing 26 letters)
            - `left` is initialized to empty list
            - `right` contains the count of each character which we will have by going through the string and incrementing the count for the particular index (ord(c) - ord('a'))
        We will need a set to store all currently found 3-letter palindromes
        Next, we have a loop that goes through each character
            - At the start of the loop, we reduce the count of the character pointed to at the current index from the `right` list
            - We also add 1 to the count of the prev character (at index: i-1) on the `left` list
            - Next, we go through list on the left, for each character, check if the count on the corresponding `right`'s index is > 0
            - If there is, add this subsequence into the set
            
        We return the length of the set
        '''
        def get_char_index(c: str) -> int:
            return ord(c) - ord('a')

        left = [0] * 26
        right = [0] * 26
        for c in s:
            right[get_char_index(c)] += 1
            
        res = set()
        for i, c in enumerate(s):
            if i > 0:
                left[get_char_index(s[i-1])] += 1
            right[get_char_index(c)] -= 1
            for j in range(26):
                if left[j] > 0 and right[j] > 0:
                    char = chr(j + ord('a'))
                    res.add(f'{char}{c}{char}')
        
        return len(res)

sol = Solution()
print(f'output: {sol.countPalindromicSubsequence("aabca")}, expected: 3')
print(f'output: {sol.countPalindromicSubsequence("adc")}, expected: 0')
print(f'output: {sol.countPalindromicSubsequence("bbcbaba")}, expected: 4')
