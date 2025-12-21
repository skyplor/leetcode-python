class Solution:
    def minOperations(self, nums: list[int]) -> int:
        '''
        For this problem, the main logic is to get the first gcd of 1 out of the list of numbers. 
        After that we will be able to transform the rest into 1 in (n - 1) operations.

        Next, we try windows of increasing size (from 2 to n). For each window, we simulate 
        reducing it by computing GCD iteratively: gcd(gcd(nums[i], nums[i+1]), nums[i+2])...
        Each GCD computation represents one operation. If we can reduce a window to GCD = 1, 
        then we know how many operations it takes to create our first 1.

        - Window size 2: requires 1 operation
        - Window size 3: requires 2 operations
        - Window size k: requires k-1 operations

        We return the minimum operations found across all windows, plus (n - 1).
        '''

        def gcd_multiple(numbers) -> int:
            result = numbers[0]

            for i in range(1, len(numbers)):
                result = gcd(result, numbers[i])

                if result == 1:
                    return result

            return result

        def gcd(n1: int, n2: int) -> int:
            '''
            Using euclidean algorithm
                - divide larger number by smaller number
                    - If remainder is 0, smaller number is GCD
                    - else, larger number = smaller number, smaller number = remainder
            '''
            large, small = n1, n2
            if n1 < n2:
                large, small = n2, n1

            remainder = large % small
            while remainder > 0:
                large = small
                small = remainder
                remainder = large % small

            return small

        n = len(nums)
        ones_count = nums.count(1)
        if ones_count > 0:
            return n - ones_count

        if gcd_multiple(nums) > 1:
            return -1

        for window_size in range(2, n+1):
            for start in range(n - window_size + 1):
                divisor = gcd_multiple(nums[start:start+window_size])
                if divisor == 1:
                    return window_size + n - 2

        return -1


sol = Solution()
print(f'output: {sol.minOperations([2, 6, 3, 4])}, expected: 4')
print(f'output: {sol.minOperations([2, 10, 6, 14])}, expected: -1')
