class Solution:
  def countSubstrings(self, s: str) -> int:
    res = 0
    for i in range(len(s)):
      # find odd palindromes
      res += self.countPalindromes(s, i, i)
      # find even palindromes
      res += self.countPalindromes(s, i, i + 1)

    return res
  
  def countPalindromes(self, s: str, l: int, r: int) -> int:
    res = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
      res += 1
      l -= 1
      r += 1
    return res
  
sol = Solution()
# s = 'abc'
s = 'aaa'
output = sol.countSubstrings(s)
print(f'output: {output}')