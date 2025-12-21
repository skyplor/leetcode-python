class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        function that returns whether this is a vowel
        list of vowels positions [0,2,5,6]
        0 <-> 6, 2 <-> 5
        mid = (length of vowels position // 2)
        create a list of characters for ease of manipulation
        do the swap, then join at the end
        '''
        def is_vowel(c: str) -> bool:
            return c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        result = []
        vowels_idx = []
        for i, c in enumerate(s):
            result.append(c)
            if is_vowel(c):
                vowels_idx.append(i)

        mid_idx = len(vowels_idx) // 2
        for i in range(0, mid_idx):
            vowel_idx, vowel_idx_to_swap = vowels_idx[i], vowels_idx[-i-1]
            result[vowel_idx], result[vowel_idx_to_swap] = result[vowel_idx_to_swap], result[vowel_idx]

        return ''.join(result)


sol = Solution()
# s = "IceCreAm"
s = "leetcode"
output = sol.reverseVowels(s)
print(f'output: {output}')
