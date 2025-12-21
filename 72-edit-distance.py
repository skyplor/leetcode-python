class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        This is a 2-D DP problem. For this, we will have 2 loops that goes through each character of each word to compare the characters
        Each iteration, we will have certain decision to make based on the following scenarios/cases:
          1. if both empty, then operation = 0
          2. if word1 is empty, it takes len(word2) operations (insert operations)
          3. if word2 is empty, it takes len(word1) operations (remove operations)
          4. if both same character, we go to the next character without +1 to the operation
          5. otherwise, we have 3 potential scenarios:
            1. remove character from word1 - that means we simply increment `i` while `j` remains. (i+1, j)
            2. insert character from word2 into word1 - that means we increment `j` while `i` remains. (i, j+1)
            3. replace character from word2 with word1 - that means we increment both `i` and `j`. (i+1, j+1)

            These scenarios corresponds to the 2-D grids, so it means grid[i][j] depends on grid[i+1][j], grid[i][j+1], grid[i+1][j+1] and we need to get the 1 + minimum operation from those grid

        e.g
          word1 = 'abd', word2 = 'acd'
                  j
                a b d
              a    
          i   c
              d

          We will need an additional row and col after as usual and we can now tabulate the last row and col

                  j
                0 1 2 3 
                a b d
            0 a       3
          i 1 c       2
            2 d       1
            3   3 2 1 0

          calculation of the last row and col are based on scenarios 1, 2, 3

          Next, we can do the actual calculation, bottom up because grid[i][j] depends on grid[i+1][j], grid[i][j+1], grid[i+1][j+1]
        '''
        n_word1 = len(word1)
        n_word2 = len(word2)
        dp = [[float('inf')] * (n_word1+1) for _ in range(n_word2+1)]

        dp[n_word2][n_word1] = 0

        for i in range(n_word2):
            dp[i][n_word1] = n_word2 - i
        for j in range(n_word1):
            dp[n_word2][j] = n_word1 - j

        for i in range(n_word2 - 1, -1, -1):
            c1 = word2[i]
            for j in range(n_word1 - 1, -1, -1):
                c2 = word1[j]
                if c2 == c1:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])

        return dp[0][0]


sol = Solution()
# word1 = 'abc'
# word2 = 'adc'
word1 = 'horse'
word2 = 'ros'
output = sol.minDistance(word1, word2)
print(f'output: {output}')
