import math

class Solution:
    def countTriples(self, n: int) -> int:
        '''
        We have 2 loops:
            first from 1 to n and the second from n1 + 1 to n 
            each time we check if the total is valid and if so, we add 2 to the result because first 2 indices can swap
        '''
        res = 0
        total_set = set()
        for i in range(1, n + 1):
            total_set.add(i**2)

        for n1 in range(1, n + 1):
            for n2 in range(n1 + 1, n + 1):
                total = n1**2 + n2**2
                if total in total_set:
                    res += 2

        return res


sol = Solution()
print(f'output: {sol.countTriples(5)}, expected: 2')
print(f'output: {sol.countTriples(10)}, expected: 4')
