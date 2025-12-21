class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        we get the length of a candidate, then we calculate how many times is needed to duplicate candidate
        '''
        l1, l2 = len(str1), len(str2)

        def valid(l: int) -> bool:
            if l1 % l > 0 or l2 % l > 0:
                return False
            # get the number of times to multiply for each str
            factor1, factor2 = l1 // l, l2 // l
            return str1[:l]*factor1 == str1 and str1[:l]*factor2 == str2

        for l in range(min(l1, l2), 0, -1):
            if valid(l):
                return str1[:l]

        return ''


sol = Solution()
# str1 = 'ABCABC'
# str2 = 'ABC'
# str1 = 'ABABAB'
# str2 = 'ABAB'
# str1 = 'LEET'
# str2 = 'CODE'
str1 = 'ABCDEF'
str2 = 'ABC'
output = sol.gcdOfStrings(str1, str2)
print(f'output: {output}')
