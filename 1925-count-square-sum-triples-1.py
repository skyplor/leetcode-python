import math


class Solution:
    def countTriples(self, n: int) -> int:
        '''
        We first pre-compute the valid `c^2` values as a set
        Next, we have 2 loops from 1 to n and each time we check if the total is in the pre-compute values and if so, we add 1 to the result
        '''
        res = 0
        total_set = set()
        for i in range(1, n + 1):
            total_set.add(i**2)

        for n1 in range(1, n + 1):
            for n2 in range(1, n + 1):
                if n2 == n1:
                    continue
                if n1**2 + n2**2 in total_set:
                    res += 1

        return res


sol = Solution()
print(f'output: {sol.countTriples(5)}, expected: 2')
print(f'output: {sol.countTriples(10)}, expected: 4')
