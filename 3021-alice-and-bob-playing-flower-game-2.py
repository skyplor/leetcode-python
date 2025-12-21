class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        '''
        Since Alice takes the first turn, and we want Alice to win the game, that means Alice should be the one to pick the last flower. That means total number of flowers has to be odd.
        Rules:
            - Minimum number of flowers on each side is 1
            - Maximum number of flowers for x is 'n'
            - Maximum number of flowers for y is 'm'
            - Total number of flowers must be ODD

        We can use pure mathematical formula for this. Extending from the previous solution, we can find the count of odd and even numbers for n and the count of odd and even numbers of m
        Next, we just multiply the odd_n with even_m as well as even_n with odd_m
        Next, we just sum both results up
        
        Time: O(1)
        Space: O(1)
        '''
        odd_n = (n+1) // 2
        odd_m = (m+1) // 2
        even_n = (n) // 2
        even_m = (m) // 2
        return odd_n * even_m + odd_m * even_n


sol = Solution()
n = 3
m = 2
print(f'output: {sol.flowerGame(n, m)}')
