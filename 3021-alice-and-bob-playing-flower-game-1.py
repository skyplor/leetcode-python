class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        '''
        Since Alice takes the first turn, and we want Alice to win the game, that means Alice should be the one to pick the last flower. That means total number of flowers has to be odd.
        Rules:
            - Minimum number of flowers on each side is 1
            - Maximum number of flowers for x is 'n'
            - Maximum number of flowers for y is 'm'
            - Total number of flowers must be ODD

        Brute force way would be to have 2 for loops for n and m, and in each iteration, we accept or reject based on the rule and increment our result counter
        Another way is to have a loop for n, and then based on whether n is odd or even, we find the values of m that can satisfy the rule of making the sum ODD.
            - We can enhance this by choosing the smaller value of the 2 (n or m) and use that as the loop instead
            
        To find all values of m that satisfy the rule, we only need to find how many times we can increment m by 2 (from either 1 or 2 depending on chosen value of n is odd or even) before reaching m.
        This way, we don't have to get the actual number, but just need get the total count
        
        e.g if m is 10, and we start at 2, that means our range is 2 to 10, total of 9 digits, (2, 4, 6, 8, 10). If we start at 1, that means our range is 1 to 10, total of 10 digits, (1, 3, 5, 7, 9)
        e.g if m is 11, and we start at 2, that means our range is 2 to 11, total of 10 digits, (2, 4, 6, 8, 10). If we start at 1, that means our range is 1 to 11, total of 11 digits, (1, 3, 5, 7, 9, 11)

        If n is odd: start at 2 and count how many times we can increment until reaching m
            - total_count = m // 2
        If n is even: start at 1 and count how many times we can increment until reaching m
            - total_count = (m+1) // 2

        Time: O(min(n, m))
        Space: O(1)
        '''
        low_val = min(n, m)
        high_val = max(n, m)
        total_count = 0
        for i in range(1, low_val+1):
            if i % 2 == 0:
                total_count += (high_val + 1) // 2
            else:
                total_count += (high_val) // 2
                
        return total_count
        
    
sol = Solution()
n = 3
m = 2
print(f'output: {sol.flowerGame(n, m)}')