class Solution:
    def totalMoney(self, n: int) -> int:
        '''
        Using a for loop, we can mod i and get the day. If it's a monday, we add from the previous monday. We can get the correct value for each monday by deducting 5 from the last known number
        '''
        result = 0
        last = 0
        for i in range(1, n + 1):
            if i % 7 == 1:
                last = max(1, last - 5)
                result += last
            else:
                last += 1
                result += last

        return result


sol = Solution()
print(f'output: {sol.totalMoney(4)}, expected: 10')
print(f'output: {sol.totalMoney(10)}, expected: 37')
print(f'output: {sol.totalMoney(20)}, expected: 96')
