import math

class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        '''
        go through each value and try to find the divisors. To find the divisors, we use another loop that goes from 1 to square root of the value.
        We use a temp running total to store the sum of existing divisors found.
        We also use a count variable to know how many divisors we found so far
        Each time it can be divided cleanly, we check if the 2nd divisor is the same
            - if same, we add into temp running total once and increment count by 1
            - else, we add both values into temp running total and increment count by 2
        If there are more than 4 divisors, we then go to the next number.
        else, at the end of the loop, we add the temp running total into a running total
        '''
        total = 0
        for n in nums:
            temp_running_total = 0
            count = 0
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    if i != n // i:
                        temp_running_total += i + (n // i)
                        count += 2
                    else:
                        temp_running_total += i
                        count += 1

                if count > 4:
                    break
                    
            if count == 4:
                total += temp_running_total
                
        return total
                    
        
sol = Solution()
print(f'output: {sol.sumFourDivisors([21,21])}, expected: 64')
print(f'output: {sol.sumFourDivisors([1,2,3,4,5])}, expected: 0')