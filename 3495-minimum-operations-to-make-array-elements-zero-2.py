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
                    - For each number, we check the number of quat_bits of that number.
                    - We then calculate how many other numbers can be represented by the number of quat_bits
                    - Number of operations to make a number 0
                        - Since we are dividing by 4 each time, we can have the base be of base 4 so this is equivalent to shifting the quat_bits to the right 1 time.
                    - So here, we are calculating bottom-up, base_4 = 1, 4, 16, 64, and at each number, how many quat_bit does it have (to calculate how many times we need to shift the quat_bit).
                    - Then we multiply by the total number of numbers that can be represented by that number of quat_bits so we know the TOTAL number of operations
        '''
        res = 0

        cache = {}
        def operations(x: int) -> int:
            if x in cache:
                return cache[x]
            base = 1
            quat_bits = 1
            ops = 0
            while base <= x:
                numbers_with_same_quat_bits_count = min(base * 4 - 1, x) - base + 1
                ops += numbers_with_same_quat_bits_count * quat_bits
                quat_bits += 1
                base *= 4

            cache[x] = ops
            return ops

        for minimum, maximum in queries:

            res += (operations(maximum) - operations(minimum-1) + 1) // 2

        return res


sol = Solution()
queries = [[1, 2], [2, 4]]
print(f'output: {sol.minOperations(queries)}, expected: 3')
queries = [[2, 6]]
print(f'output: {sol.minOperations(queries)}, expected: 4')
