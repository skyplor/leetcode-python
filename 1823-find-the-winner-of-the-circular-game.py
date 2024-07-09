class Solution:
  def findTheWinner(self, n: int, k: int) -> int:
    '''
    we can use first use recursive to solve this
    each round, we reduce by 1 and start from the next element
    '''
    # def winnerHelper(n, k):
    #   if n == 1:
    #     return 0
    #   return (winnerHelper(n-1, k) + k) % n
    
    # return winnerHelper(n, k) + 1
    
    '''
    Next, we use iterative way for this
    '''
    ans = 0
    for i in range(1, n + 1):
      ans = (ans + k) % i
      
    return ans + 1
  
sol = Solution()
# n = 5
# k = 2
n = 6
k = 5
print(f'output: {sol.findTheWinner(n, k)}')