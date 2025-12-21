class Solution:
    def minOperations(self, queries: list[list[int]]) -> int:
        '''
        Brute force:
            - Loop through each query, expand the numbers from the given range
            - For each number, we will need to calculate how many times we need to do the floor division to make it 0
            - Add each number in the range into a max_heap and each time we pop 2 elements from the heap, do the division, then if > 0, push the number back

        But Brute force will result in TLE

        Opimised:
            - For each query,
                - We get total number of individual operations for all numbers from 1 to max (inclusive)
                - We get total number of individual operations for all numbers from 1 to min - 1 (inclusive)
                - Then we subtract the operations to get the total number of individual operations for all numbers from min to max (inclusive)
                - Then we get the total operations if we work on 2 numbers at a time
                    - (operations + 1) // 2

                - To calculate the total number of individual operations from 1 to x
                    - For each number, we check the number of bits of that number.
                    - We then calculate how many other numbers can be represented by the number of bits
                    - Number of operations to make a number 0
                        - Since we are dividing by 4 each time, it is equivalent to shifting the bit to the right 2 times.
                    - So here, we are calculating bottom-up, base = 1, 2, 4, 8, and at each number, how many bits does it have (to calculate how many times we need to shift the bits 2 times).
                    - Then we multiply by the total number of numbers that can be represented by that number of bits so we know the TOTAL number of operations
        '''
        res = 0

        def operations(x: int) -> int:
            base = 1
            bits = 1
            ops = 0
            while base <= x:
                numbers_with_same_bit_count = min(base * 2 - 1, x) - base + 1
                number_of_bits = (bits + 1) // 2
                ops += numbers_with_same_bit_count * number_of_bits
                bits += 1
                base *= 2

            return ops

        for minimum, maximum in queries:

            res += (operations(maximum) - operations(minimum-1) + 1) // 2

        return res


sol = Solution()
queries = [[1, 2], [2, 4]]
print(f'output: {sol.minOperations(queries)}, expected: 3')
queries = [[2, 6]]
print(f'output: {sol.minOperations(queries)}, expected: 4')
