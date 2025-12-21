from typing import List

class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    '''
    What can we take away from the description?
    
    `You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.`

    - This is a minimization problem — we want to find the fewest number of coins that sum up to amount.
    - the word "fewest" should be a hint that maybe dynamic programming would help us get to an answer.
    
    `Return the fewest number of coins that you need to make up that amount. If that amount cannot be made up by any combination of the coins, return -1.`

    - Okay so with dynamic programming in mind, we see we have an invalid case. how do we handle this?
    - Not all values are guaranteed to be reachable. This hints that we may need a sentinel value to represent an impossible state.
    - We also know that we're not returning the actual combination of coins — just the minimum count.
    
    `You may assume that you have an infinite number of each kind of coin.`

    - That's an important signal: this is an unbounded knapsack problem, which naturally fits dynamic programming.
    
    Let's say we're trying to compute dp[7] and we have coins [1, 2, 5].

    If we use coin 1, then we need to know how many coins it takes to make dp[6].
    If we use coin 2, we look at dp[5], and so on.

    So the recurrence becomes:

    dp[i] = min(dp[i], dp[i - coin] + 1)

    We add +1 to account for the coin we just used.

    To handle unreachable amounts, we initialize all dp[i] to a large number (amount + 1), and at the end, check if dp[amount] was updated.
    '''
    # using a 1-d dp
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
      for c in coins:
        if (a - c) >= 0:
          dp[a] = min(dp[a], 1 + dp[a - c])
          
    return dp[amount] if dp[amount] != (amount + 1) else -1
    
  
sol = Solution()
coins = [1,2,5]
amount = 11
output = sol.coinChange(coins, amount)
print(f'coins: {coins}\namount: {amount}\noutput: {output}')