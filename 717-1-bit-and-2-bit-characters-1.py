class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        '''
        We have a loop that goes through each bit and at each index, we determine if we can use 1 index or requires 2 indices
        Base case is when i == n - 2, we check if it is possible for us to use both bits. If yes, return False
        '''
        n = len(bits)
        if n == 1:
            return True
        
        def recurse(i: int) -> bool:
            if i == n:
                return True
            if ((i == n - 1) or (i == n - 2)) and bits[i] == 1:
                return False
            
            res = True
            if bits[i] == 0:
                res = res and recurse(i+1)
                
            if bits[i] == 1 and i + 2 < n:
                res = res and recurse(i+2)
            
            return res
        
        return recurse(0)
                


sol = Solution()
print(f'output: {sol.isOneBitCharacter([1, 0, 0])}, expected: True')
print(f'output: {sol.isOneBitCharacter([1, 1, 1, 0])}, expected: False')
print(f'output: {sol.isOneBitCharacter([1, 1, 0])}, expected: True')
