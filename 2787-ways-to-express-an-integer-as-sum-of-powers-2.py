class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        '''
        We can go with recursion for a start and then we optimise from there by adding memoization and subsequently change it to iteration

        We will need a recursion function that takes in an index and the max limit
        Base case:
            - it will be when the value == max limit, then we can increment res counter by 1
            - The next thing is if the value exceeds max limit, then we can just return
            - If the value is below the max limit, we can choose to either take this value or don't take the value.
                - if we don't take the value, we just proceed to increment the index by 1 and call the function again
                - if we take the value, then we will reduce the max_limit and call the function again

        '''
        starting_index = int(n ** (1/x))
        while (starting_index + 1) ** x <= n:
            starting_index += 1
        while starting_index ** x > n:
            starting_index -= 1

        dp = [[-1] * (n+1) for _ in range(starting_index+1)]
        MOD = 10 ** 9 + 7

        def recursive(i: int, limit: int) -> int:

            if i < 1:
                return 1 if limit == 0 else 0

            if dp[i][limit] != -1:
                return dp[i][limit]

            notake = recursive(i-1, limit)

            take = 0
            value = i ** x
            if limit - value >= 0:
                take = recursive(i-1, limit - value)

            result = take + notake
            dp[i][limit] = result
            return result

        res = recursive(starting_index, n)

        return res % MOD


sol = Solution()
print(f'output: {sol.numberOfWays(64, 3)}')
# print(f'output: {sol.numberOfWays(4, 1)}')
