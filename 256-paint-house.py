class Solution:
    def min_cost(self, costs: list[list[int]]) -> int:
        '''
        To solve this problem, we can simulate using a decision tree. Each time we paint a house, the next house must be painted with the other 2 colors and not the current color.
        e.g. [[14,2,11],[11,14,5],[14,3,10]]
                                                                  .
                                    /                             |                           \\
                                 (i=0)                          (i=1)                        (i=2) 
        house 0                    14                             2                            11
                              /           \\                 /          \\                 /         \\
                            (i=1)        (i=2)            (i=0)        (i=2)            (i=0)        (i=1)
        house 1              14            5               11            5               11            14
                          /      \\     /     \\       /      \\      /      \\       /      \\     /      \\
                        (i=0)  (i=2)  (i=0)  (i=1)   (i=1)   (i=2)  (i=0)   (i=1)   (i=1)   (i=2) (i=0)   (i=2)
        house 2          14     10     14      3       3      10      14      3       3       10    14      10

        With this, we can see that it is possible to break up into sub-problems to get the minimum cost to paint the current house + minimum cost to paint the houses before it.
        So if it's to paint house 0, it's simple as there's no other house before it, so this is our base case
        And in order for us to know the costs, we need 2 different factors. house number and the index. So we can use a 2-D DP for this
        It will be a [n by 3] matrix
        The logic behind:
            - Create a 2-d dp array
            - each house is a row of the 2-d array. We populate the base case for row=0 with costs[0]
            - next, for row=1,col=0, we will need to get the minimum cost that we have calculated for row=0, col=1 & col=2 and add the current cost to it to get the minimum cost
            - continue with the calculation for all rows and cols
            - we will return the minimum cost of the last row

        Note: we can further optimise this by improving on the space complexity to O(1) instead of the current O(n*3)
            - When we are calculating the cost for a cell, we are only concern with the values in the row directly before this, that means we can store just the prev row's values
            - So each time we move to the next row, we just replace what we have calculated into the prev_values
        '''
        dp = [val for val in costs[0]]
        n = len(costs)
        for house in range(1, n):
            dp0 = costs[house][0] + min(dp[1], dp[2])
            dp1 = costs[house][1] + min(dp[0], dp[2])
            dp2 = costs[house][2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2]

        return min(dp)
    
sol = Solution()
costs = [[14,2,11],[11,14,5],[14,3,10]]
output = sol.min_cost(costs)
print(f'output: {output}')
