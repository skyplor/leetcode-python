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
        
        This is an optimization of the previous by tracking the characters that are actually available on the right and only iterating through available characters on the left instead of all 26 characters
        We use a `left` set and `right` set and a `right_count` list that will contain the actual count. Whenever count reaches 0, we remove from the `right` set
        '''
        def get_char_index(c: str) -> int:
            return ord(c) - ord('a')

        left = set()
        right = set(s)
        right_count = [0] * 26
        for c in s:
            right_count[get_char_index(c)] += 1
            
        res = set()
        for i, c in enumerate(s):
            if i > 0:
                left.add(s[i-1])
            right_count[get_char_index(c)] -= 1
            if right_count[get_char_index(c)] == 0:
                right.discard(c)
            for left_c in left:
                if left_c in right:
                    res.add(f'{left_c}{c}{left_c}')
        
        return len(res)

sol = Solution()
print(f'output: {sol.countPalindromicSubsequence("aabca")}, expected: 3')
print(f'output: {sol.countPalindromicSubsequence("adc")}, expected: 0')
print(f'output: {sol.countPalindromicSubsequence("bbcbaba")}, expected: 4')
