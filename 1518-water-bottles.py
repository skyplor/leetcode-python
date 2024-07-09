class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles >= numExchange:
            exchangedBottles = numBottles // numExchange
            res += exchangedBottles
            numBottles = exchangedBottles + numBottles % numExchange

        return res

sol = Solution()
numBottles = 9
numExchange = 3
print(f'output: {sol.numWaterBottles(numBottles, numExchange)}')