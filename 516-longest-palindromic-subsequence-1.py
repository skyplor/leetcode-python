class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        We can use dp for this. But first, let's start with recursion to get our base case
        We can use recursion with base case of 1 letter. And we return 1 since it is a palindrome
        '''

        def get_longest_subsequence(s: str) -> int:
            n = len(s)
            if n < 2:
                return n

            if s[0] == s[-1]:
                return get_longest_subsequence(s[1:-1]) + 2
            else:
                return max(get_longest_subsequence(s[1:]), get_longest_subsequence(s[:-1]))

        return get_longest_subsequence(s)


sol = Solution()
s = 'bbbab'
print(f'output: {sol.longestPalindromeSubseq(s)}, expected: 4')
s = 'cbbd'
print(f'output: {sol.longestPalindromeSubseq(s)}, expected: 2')
