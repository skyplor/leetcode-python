from typing import List
from collections import deque


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        '''
        - Might need to reverse the array so that it's easier for us to do the multiplication using the index.
        - Another way is to get the length and minus that with the current index to use it as the exponent (more efficient)
        - need 2 functions to convert from negabinary to decimal and vice versa
        - convert negabinary to decimal
            - loop through with the index and use -2 ** (len(arr) - i)
            - sum up all the numbers and return

        - convert decimal to negabinary
            - we will use division and modulus for this to get the representation array
            - Mod will give us the bit whether it's 0 or 1. Next we divide the number by -2 to get the number to process for the next loop. we need to round to whole number as well
            - e.g
                1. -2: [1, 0]
                    -2 % 2 = 0
                        -2 // 2 = -1 # NOTE: instead of using (number //= -2) performing floor division with negative number, it is safer to first perform floor division with positive number then flip the bit
                        -1 * -1 = 1
                    1 % 2 = 1
                        1 // 2 = 0
                        0 * -1 = 0

                2. -4: [1,1,0,0] (we set the bit for higher significant bits so it's (-8) + (4) = -4)
                    -4 % 2 = 0
                        -4 // 2 = -2
                        -2 * -1 = 2
                    2 % 2 = 0
                        2 // 2 = 1
                        1 * -1 = -1
                    -1 % 2 = 1
                        -1 // 2 = -1
                        -1 * -1 = 1
                    1 % 2 = 1
                        1 // 2 = 0
                        0 * -1 = 0
        '''
        def to_decimal(arr: List[int]) -> int:
            n = len(arr) - 1
            res = 0
            for i, num in enumerate(arr):
                exponent = n - i
                res += num * ((-2) ** exponent)

            return res

        def to_negabinary(number: int) -> List[int]:
            if number == 0:
                return [0]

            res = deque()
            while number != 0:
                res.appendleft(number % 2)
                # NOTE: instead of using (number //= -2) performing floor division with negative number, it is safer to first perform floor division with positive number then flip the bit
                number //= 2
                number *= -1

            return list(res)

        return to_negabinary(to_decimal(arr1) + to_decimal(arr2))


sol = Solution()
arr1 = [1, 1, 1, 1, 1]
arr2 = [1, 0, 1]
output = sol.addNegabinary(arr1, arr2)
print(f'output: {output}')
