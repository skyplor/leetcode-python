import math

class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        '''
        I will have a loop that will continue as long as the variable `should_check` is set. Whenever a pair of co-primes is found, we set the `should_check` to True
        Within the while loop, we have a for loop that goes through the list from idx 1 to n-1, each time checking (i-1 & i).
        At the start of the for loop we will set the should_check as False

        We need a function to check if 2 numbers are non-coprime
            - GCD(x, y) > 1
        We can have a function that get LCM of 2 non-coprime numbers
        Then we just replace the 2 numbers with the LCM returned from the function
        '''
        def is_non_coprime(n1: int, n2: int) -> bool:
            return math.gcd(n1, n2) > 1

        def compute_lcm(n1: int, n2: int) -> int:
            return math.lcm(n1, n2)

        idx = len(nums) - 2
        while idx >= 0:
                
            if idx == len(nums) - 1 or not is_non_coprime(nums[idx], nums[idx+1]):
                idx -= 1
                continue

            lcm = compute_lcm(nums[idx], nums[idx+1])
            nums[idx+1] = lcm
            del nums[idx]

        return nums


sol = Solution()
nums = [6, 4, 3, 2, 7, 6, 2]
print(f'output: {sol.replaceNonCoprimes(nums)}, expected: [12, 7, 6]')
nums = [2, 2, 1, 1, 3, 3, 3]
print(f'output: {sol.replaceNonCoprimes(nums)}, expected: [2, 1, 1, 3]')
