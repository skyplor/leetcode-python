class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        '''
        We first need to determine if the first complexity is the minimum and is unique
        If no, then return 0
        If yes, we return (n-1)! since there are n-1 ways to permutate
        '''
        n = len(complexity)
        first = complexity[0]
        for i in range(1, n):
            c = complexity[i]
            if c <= first:
                return 0

        res = 1
        for i in range(1, n):
            res = (res * i) % (10 ** 9 + 7)

        return res


sol = Solution()
print(f'output: {sol.countPermutations([1, 2, 3])}, expected: 2')
print(f'output: {sol.countPermutations([3, 3, 3, 4, 4, 4])}, expected: 0')
print(f'output: {sol.countPermutations([38, 223, 100, 123, 406, 234, 256, 93, 222, 259, 233, 69, 139, 245, 45, 98, 214])}, expected: 789741546')
