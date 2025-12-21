class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            temp = ''
            for i in range(len(s) - 1):
                temp += str((ord(s[i]) - ord('0') +
                            ord(s[i+1]) - ord('0')) % 10)

            s = temp

        return s[0] == s[1]


sol = Solution()
print(f'output: {sol.hasSameDigits('3902')}, expected: True')
print(f'output: {sol.hasSameDigits('34789')}, expected: False')
