class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        '''
        We will follow the simulation as specified
        '''

        ops = 0
        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1

            ops += 1

        return ops


sol = Solution()
print(f'output: {sol.countOperations(num1=2, num2=3)}, expected: 3')
print(f'output: {sol.countOperations(num1=10, num2=10)}, expected: 1')
