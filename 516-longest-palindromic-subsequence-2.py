class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        We can use dp for this. But first, let's start with recursion to get our base case
        We can use recursion with base case of 1 letter. And we return 1 since it is a palindrome
        '''

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        def solve(l: int, r: int) -> int:
            if l > r:
                return 0
            if l == r:
                return 1

            if dp[l][r] > 0:
                return dp[l][r]

            if s[l] == s[r]:
                dp[l][r] = solve(l+1, r-1) + 2
            else:
                dp[l][r] = max(solve(l+1, r), solve(l, r-1))

            return dp[l][r]

        return solve(0, n-1)


sol = Solution()
s = 'bbbab'
print(f'output: {sol.longestPalindromeSubseq(s)}, expected: 4')
s = 'cbbd'
print(f'output: {sol.longestPalindromeSubseq(s)}, expected: 2')
