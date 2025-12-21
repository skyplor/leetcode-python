from heapq import heappush, heappop


class Solution:
    def sortVowels(self, s: str) -> str:
        '''
        First, we can have a vowel_count and each time we encounter a vowel, we add increment the count for that vowel
        Next, we go through the string again and if we encounter a vowel, we take the next vowel that exists based on the VOWELS sequence and replace with the character

        Time: O(N)
        Space: O(1)
        '''
        VOWELS = 'AEIOUaeiou'
        vowel_count = {k: 0 for k in VOWELS}

        res = ''
        for c in s:
            if c in VOWELS:
                vowel_count[c] += 1

        index = 0
        for c in s:
            if c in VOWELS:
                while vowel_count[VOWELS[index]] == 0:
                    index += 1
                current_vowel = VOWELS[index]
                res += current_vowel
                vowel_count[current_vowel] -= 1
            else:
                res += c

        return res


sol = Solution()
s = "lEetcOde"
print(f'output: {sol.sortVowels(s)}, expected: lEOtcede')
s = "lYmpH"
print(f'output: {sol.sortVowels(s)}, expected: lYmpH')
