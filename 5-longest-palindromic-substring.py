class Solution:
  def longestPalindrome(self, s: str) -> str:
    '''
    to find longest palindrome for whole string,
    we go through each character, then expand outwards
    we will need to handle both odd and even palindrome so we need to have 1 single character + expand outwards, and 2 characters + expand outwards
    '''
    res = ''
    for i in range(len(s)):
      # check odd palindrome
      l, r = i, i
      while l >= 0 and r < len(s) and s[l] == s[r]:
        if len(res) < r - l + 1:
          res = s[l:r + 1]
        l -= 1
        r += 1
        
      # check even palindrome
      if i + 1 < len(s) and s[i] == s[i+1]:
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
          if len(res) < r - l + 1:
            res = s[l:r + 1]
          l -= 1
          r += 1
          
    return res

sol = Solution()
# s = 'babad'
s = 'cbbd'
output = sol.longestPalindrome(s)
print(f'output: {output}')