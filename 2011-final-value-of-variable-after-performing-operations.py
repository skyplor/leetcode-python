class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        '''
        We just need to go through each element and add 1 if we see '+' and deduct 1 if we see '-'
        '''
        res = 0
        for op in operations:
            if '+' in op:
                res += 1
            else:
                res -= 1
        
        return res


sol = Solution()
print(
    f'output: {sol.finalValueAfterOperations(["--X", "X++", "X++"])}, expected: 1')
print(
    f'output: {sol.finalValueAfterOperations(["++X", "++X", "X++"])}, expected: 3')
print(
    f'output: {sol.finalValueAfterOperations(["X++", "++X", "--X", "X--"])}, expected: 0')
