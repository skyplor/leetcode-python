class Solution:
    def countOdds(self, low: int, high: int) -> int:
        '''
        We get the total count of numbers from low to high and divide by 2. If low is odd, add 1 to the res
        '''
        length = high - low + 1
        res = length // 2
        if low % 2 and length % 2:
            res += 1

        return res


sol = Solution()
print(f'output: {sol.countOdds(3, 7)}, expected: 3')
print(f'output: {sol.countOdds(8, 10)}, expected: 1')
print(f'output: {sol.countOdds(21, 22)}, expected: 1')
