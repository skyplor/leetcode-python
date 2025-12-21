class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        '''
        Using a set, add the numbers in and each time check if set already had that number. 
        We use a list to keep track of duplicated numbers and add it in if found
        '''
        res = []
        existing = set()
        for num in nums:
            if num not in existing:
                existing.add(num)
            else:
                res.append(num)
        return res

sol = Solution()
print(f'output: {sol.getSneakyNumbers([0, 1, 1, 0])}, expected: [0, 1]')
print(f'output: {sol.getSneakyNumbers([0, 3, 2, 1, 3, 2])}, expected: [2, 3]')
print(
    f'output: {sol.getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2])}, expected: [4, 5]')
