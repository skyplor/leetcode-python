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
    if n <= 3:
      return n
    
    n1, n2 = 2, 3
    for _ in range(4, n+1):
      temp = n1 + n2
      n1 = n2
      n2 = temp
    
    return temp
  
sol = Solution()
n = 5
output = sol.climbStairs(n)
print(f'n: {n}\noutput: {output}')