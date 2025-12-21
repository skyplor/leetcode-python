class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        '''
        We can think of this as how many times we need to perform `num1 - (2ⁱ + num2) = 0`
            - num1 = (2ⁱ⁰ + num2) + (2ⁱ¹ + num2) + (2ⁱ² + num2) + ... + (2ⁱᵏ + num2)
            - num1 = k(num2) + 2ⁱ⁰ + 2ⁱ¹ + 2ⁱ² + ... + 2ⁱᵏ
            - num1 - k(num2) = 2ⁱ⁰ + 2ⁱ¹ + 2ⁱ² + ... + 2ⁱᵏ
            - num1 - k(num2) = sum of k powers of 2
        
        IF our LHS is 10, 2's complement = 1010
            - What is the minimum number of operations needed to transform from 0000 to 1010? Minimum is 2 because we need to set the bits individually.
        
        Now for the RHS of the equation:
            e.g
                - 2⁰ + 2⁰ = 2¹ (2's complement: 10)
                - 2¹ (2's complement: 10)
                    - So minimum number of operation to set number to 2 is `1` because we can either do `2⁰ + 2⁰` or `2¹`
                - 2⁰ + 2¹ = 3 (2's complement: 11)
                    - Minimum number of operation to set number to 3 is `2`
                
        So what we can do is to have a loop that goes through each value of `k`, and then we check if the total value we get on the LHS can be represented in 2's complement by k number of 1s
            - A number `x` can be a sum of `k` powers of 2 IFF:
                1. Number of `1s` bit of x <= k
                    - Why "<=" ? Because for the `2¹` bit to be a 1, it can either be `2⁰ + 2⁰` or `2¹`.
                    - If we have 3 `1s` bit, the minimum is 3. But k can be more than 3. So k >= 3
                2. k <= x
                    - Why k must be <= x? because we can't use xth bit more than once to add up to x
                    
        Since the question provided an upper bound of 60, we can treat 60 as the maximum number of iterations for us to try
        '''
        
        for k in range(1, 61):
            x = num1 - (k * num2)
            if x.bit_count() <= k and k <= x:
                return k
            
        return -1
            
    
sol = Solution()
num1 = 3
num2 = -2
print(f'output: {sol.makeTheIntegerZero(num1, num2)}, expected: 3')
num1 = 5
num2 = 7
print(f'output: {sol.makeTheIntegerZero(num1, num2)}, expected: -1')