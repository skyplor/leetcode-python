from heapq import heappush, heappop


class Solution:
    def sortVowels(self, s: str) -> str:
        '''
        First, we can have a s_vowels and each time we encounter a vowel, we add into the array
        Next, we sort the array
        Lastly, we go through the string again and if we encounter a vowel, we take the next vowel and replace with the character

        Time: O(N log N)
        Space: O(N)
        '''
        VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_vowels = []
        res = ''
        for c in s:
            if c in VOWELS:
                s_vowels.append(c)

        s_vowels.sort()
        index = 0
        for c in s:
            if c in VOWELS:
                res += s_vowels[index]
                index += 1
            else:
                res += c

        return res


sol = Solution()
s = "lEetcOde"
print(f'output: {sol.sortVowels(s)}, expected: lEOtcede')
s = "lYmpH"
print(f'output: {sol.sortVowels(s)}, expected: lYmpH')
