class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        '''
        We can use a while loop and a variable representing the cur_bottles that is empty
        We exit the while loop when the cur_bottles < numExchange
        '''
        total = numBottles
        remaining = 0
        while numBottles + remaining >= numExchange:
            numBottles += remaining
            temp = numBottles % numExchange
            numBottles //= numExchange
            remaining = temp
            total += numBottles
            
        return total

sol = Solution()
numBottles = 9
numExchange = 3
print(f'output: {sol.numWaterBottles(numBottles, numExchange)}, expected: 13')
numBottles = 15
numExchange = 4
print(f'output: {sol.numWaterBottles(numBottles, numExchange)}, expected: 19')