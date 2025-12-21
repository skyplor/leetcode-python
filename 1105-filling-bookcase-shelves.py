from typing import List

class Solution:
  def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
    # Solution 1
    '''
    Using DP, dp[shelf_i] = height + min(dp[shelf_i+1], dp[shelf_i+2], ...)
    '''
    # dp = {}
    # def helper(i):
    #   if i == len(books):
    #     return 0
    #   if i in dp:
    #     return dp[i]

    #   cur_width = shelfWidth
    #   max_height = 0
    #   dp[i] = float('inf')
    #   for j in range(i, len(books)):
    #     next_width, next_height = books[j]
    #     if next_width > cur_width:
    #       break
    #     cur_width -= next_width
    #     max_height = max(max_height, next_height)
    #     dp[i] = min(dp[i], helper(j+1) + max_height)

    #   return dp[i]

    # Solution 2: bottom-up enhancement of Solution 1
    dp = [0] * (len(books) + 1)
    for i in range(len(books) - 1, -1, -1):
      cur_width = shelfWidth
      max_height = 0
      dp[i] = float('inf')

      for j in range(i, len(books)):
        next_width, next_height = books[j]
        if next_width > cur_width:
          break
        cur_width -= next_width
        max_height = max(max_height, next_height)
        dp[i] = min(dp[i], dp[j+1] + max_height)
    
    return dp[0]

sol = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4
print(f'output: {sol.minHeightShelves(books, shelfWidth)}')