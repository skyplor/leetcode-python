class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        We can use dp for this and do this iteratively starting with string of smaller length
        We need to then find out where to start the string from for each length.
            - for a string of length l, if we start from i, and we want to iterate up to n (exclusive)
            - i, i + 1, ..., i + length - 1
            - if i < n, that means i + length - 1 < n
                - i < n - length + 1
                
            - For the ending index `j`:
                - j = (i + length) - 1
        '''
        n = len(s)
        if n < 2:
            return n

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]


sol = Solution()
s = 'bbbab'
print(f'output: {sol.longestPalindromeSubseq(s)}, expected: 4')
s = 'cbbd'
print(f'output: {sol.longestPalindromeSubseq(s)}, expected: 2')
