class Solution:
  def climbStairs(self, n: int):
    '''
    base case:
      if n == 1: return 1 [[1]]
      if n == 2: return 2 [[11], [2]]
    n = 3: (n = 2) + (n = 1) [[111], [12], [21]]
    n = 4: (n = 3) + (n = 2) [[1111], [121], [112], [211], [22]]
    n = 5: (n = 4) + (n = 3) [[11111], [1211], [1121], [1112], [2111], [221], [212], [122]]
    dp[n] = dp[n-1] + dp[n-2]
    '''
    dp = {}
    def recurse(n):
      if n == 1: return 1
      if n == 2: return 2
      
      if n-1 in dp:
        n1 = dp[n-1]
      else:
        n1 = recurse(n-1)
        dp[n-1] = n1

      if n-2 in dp:
        n2 = dp[n-2]
      else:
        n2 = recurse(n-2)
        dp[n-2] = n2

      return n1 + n2
    
    return recurse(n)
  
sol = Solution()
n = 5
output = sol.climbStairs(n)
print(f'n: {n}\noutput: {output}')