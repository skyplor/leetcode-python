class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        to find longest palindrome for whole string,
        we go through each character, then expand outwards
        we will need to handle both odd and even palindrome so we need to have 1 single character + expand outwards, and 2 characters + expand outwards
        '''
        def get_palindrome(left: int, right: int) -> str:
            while left in range(n) and right in range(n) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        result = ''
        n = len(s)
        for i in range(n):
            # Even
            even_palindrome = get_palindrome(i, i + 1)

            # Odd
            odd_palindrome = get_palindrome(i, i)

            for palindrome in [even_palindrome, odd_palindrome]:
                if len(palindrome) > len(result):
                    result = palindrome

        return result

sol = Solution()
# s = 'babad'
s = 'cbbd'
output = sol.longestPalindrome(s)
print(f'output: {output}')