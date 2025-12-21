class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        '''
        We have a loop that goes through each bit and at each index, we determine if we can increment by 1 or 2
        '''
        n = len(bits)

        i = 0
        while i < n - 1:
            if bits[i] == 0:
                i += 1
                continue

            i += 2

        return i == n - 1


sol = Solution()
print(f'output: {sol.isOneBitCharacter([1, 0, 0])}, expected: True')
print(f'output: {sol.isOneBitCharacter([1, 1, 1, 0])}, expected: False')
print(f'output: {sol.isOneBitCharacter([1, 1, 0])}, expected: True')
