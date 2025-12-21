class Solution:
    def climbStairs(self, n: int):
        '''
        we can use dp for this.
        it will always be number of ways for (n-1) + number of ways for (n-2)
        base case will be n < 4: return n
        '''
        memo = {i: i for i in range(4)}

        for i in range(4, n+1):
            if i in memo:
                return memo[i]

            memo[i] = memo[i-2] + memo[i-1]

        return memo[n]


sol = Solution()
n = 4
output = sol.climbStairs(n)
print(f'n: {n}\noutput: {output}')
