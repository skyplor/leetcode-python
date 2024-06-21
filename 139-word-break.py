from typing import List

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    '''
    using dp, at each index, we want to know if we can match to any of the words in the wordDict
    e.g
      s = 'neetcode', wordDict = ['neet', 'leet', 'code']
      dp[8] = True
      dp[7] = False
      dp[6] = False
      dp[5] = False
      dp[4] = True -- matches with 'code'
      dp[3] = False
      dp[2] = False
      dp[1] = False
      dp[0] = True AND (dp[0 + len(word)] = dp[4]) = True
    '''
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    for i in range(len(s))[::-1]:
      for w in wordDict:
        if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
          dp[i] = dp[i + len(w)]
          
        if dp[i]:
          break
        
    return dp[0]

sol = Solution()
# s = 'leetcode'
# wordDict = ['leet', 'code']
s = 'abcd'
wordDict = ['a', 'abc', 'b', 'cd']
output = sol.wordBreak(s, wordDict)
print(output)