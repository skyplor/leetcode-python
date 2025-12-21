class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        '''
        Each time we make an exchange, numExchange increases by 1
        '''
        bottlesDrank = 0
        emptyBottles = 0
        while numBottles + emptyBottles >= numExchange:
            bottlesDrank += numBottles
            emptyBottles += numBottles
            numBottles = 0
            while emptyBottles >= numExchange:
                emptyBottles -= numExchange
                numExchange += 1
                numBottles += 1

        return bottlesDrank + numBottles


sol = Solution()
print(f'output: {sol.maxBottlesDrunk(13, 6)}, expected: 15')
print(f'output: {sol.maxBottlesDrunk(10, 3)}, expected: 13')
