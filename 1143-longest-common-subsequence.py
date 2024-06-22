class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    '''
       a, c, d
    a [3, 2, 1]
    b [2, 2, 1]
    c [2, 2, 1]
    d [1, 1, 1]
    e [0, 0, 0]
    '''
    rows, cols = len(text1), len(text2)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    # check the right and bottom values and get the max
    # if current characters matches, add 1 to the max value and set dp's cell
    for row in range(rows - 1, -1, -1):
      for col in range(cols - 1, -1, -1):
        text1Char = text1[row]
        text2Char = text2[col]
        if text1Char == text2Char:
          dp[row][col] = 1 + dp[row + 1][col + 1]
        else:
          dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        
    return dp[0][0]
  
sol = Solution()
# text1 = 'abcde'
# text2 = 'ace'
# text1 = 'abc'
# text2 = 'def'
text1 = "bsbininm"
text2 = "jmjkbkjkv"
output = sol.longestCommonSubsequence(text1, text2)
print(f'output: {output}')