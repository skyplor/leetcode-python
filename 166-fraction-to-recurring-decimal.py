class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        '''
        How do we realise that the sequence is a repeating sequence?
        If we do the standard long division,
            e.g 4 / 333
                - since numerator (4) is lesser than denominator (333), we multiply it by 10 and check again
                - 40 < 333, multiply by 10 again
                - 400 >= 333, 400 / 333, get the int value (1), 400 mod 333 = 67
                - 67 < 333, multiply by 10
                - 670 >= 333, int(670 / 333) = 2, 670 mod 333 = 4 (there's a repeat here)

            So we will store each numerator in a seen hashmap coupled with the division int value
            modulus results:
                1. 4
                2. (0) 40
                3. (1) 67
                4. (2) 4
                5. (0) 40
                6. (1) 67
                7. (2) 4

        '''
        if numerator == 0:
            return "0"

        result = []
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            result.append('-')

        numerator = abs(numerator)
        denominator = abs(denominator)
        # Handle integer part first
        div_result, remainder = divmod(numerator, denominator)
        if numerator >= denominator:
            result.append(str(div_result))
            if remainder > 0:
                result.append('.')
            else:
                return ''.join(result)
        else:
            result.append('0.')

        # We track the index when we found a repeating remainder
        seen = {}

        while remainder > 0:
            if remainder in seen:
                result.insert(seen[remainder], '(')
                result.append(')')
                break

            seen[remainder] = len(result)
            numerator = remainder * 10
            div_result, remainder = divmod(numerator, denominator)

            result.append(str(div_result))

        return ''.join(result)


sol = Solution()
print(f'output: {sol.fractionToDecimal(1, 2)}, expected: 0.5')
print(f'output: {sol.fractionToDecimal(2, 1)}, expected: 2')
print(f'output: {sol.fractionToDecimal(4, 333)}, expected: 0.(012)')
print(f'output: {sol.fractionToDecimal(1, 6)}, expected: 0.1(6)')
print(f'output: {sol.fractionToDecimal(-50, 8)}, expected: -6.25')
print(f'output: {sol.fractionToDecimal(50, -8)}, expected: -6.25')
