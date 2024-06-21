class Solution:
  def numDecodings(self, s: str) -> int:
    '''
    using bottom-up approach, loop each character + check next character.
      if character = 0, we can ignore the rest of the string
      if character = 1, next character can be 0 - 9
      if character = 2, next character can be 0 - 6
      else (3 and above), it can only be a single character
    '''
    dp = {len(s): 1}
    for i in range(len(s) - 1, -1, -1):
      if s[i] == '0':
        dp[i] = 0
      else:
        dp[i] = dp[i + 1]
      if i + 1 < len(s) and (
        s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456'
      ):
        dp[i] += dp[i+2]
        
    return dp[0]
  
sol = Solution()
# s = '226'
s = '10'
output = sol.numDecodings(s)
print(f'output: {output}')