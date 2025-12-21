class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        create a set that contains the vowels
        create a result that is a list of the characters of the string
        we use 2 pointers, 1 point to the start, another to the end, and we increment/decrement respectively.
        When 1 hits a vowel, stop the pointer while the other continue. 
        When both reach a vowel, we swap them.
        Continue and stop once i > j
        '''

        result = list(s)
        vowel_set = set('aeiouAEIOU')
        i, j = 0, len(result) - 1
        while i < j:
            left = result[i]
            right = result[j]
            left_is_vowel = left in vowel_set
            right_is_vowel = right in vowel_set
            if left_is_vowel and right_is_vowel:
                result[i], result[j] = result[j], result[i]
                i += 1
                j -= 1

            else:
                if not left_is_vowel:
                    i += 1
                if not right_is_vowel:
                    j -= 1

        return "".join(result)


sol = Solution()
# s = "IceCreAm"
s = "leetcode"
output = sol.reverseVowels(s)
print(f'output: {output}')
