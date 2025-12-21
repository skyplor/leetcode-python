class Solution:
    def sumZero(self, n: int) -> list[int]:
        '''
        We can start from an integer 0, then expand out left and right if n is odd. But if it's even, we just expand left and right but don't include 0
        '''
        res = []
        count = 0
        if n % 2 == 0:
            count = n // 2
        else:
            count = (n-1) // 2
            res.append(0)

        left = right = 0
        for _ in range(count):
            left -= 1
            right += 1
            res.append(left)
            res.append(right)

        return res


sol = Solution()
n = 5
print(
    f'output: {sol.sumZero(n)}, expected: [-7,-1,1,3,4], [-5,-1,1,2,3] or [-3,-1,2,-2,4]')
n = 3
print(f'output: {sol.sumZero(n)}, expected: [-1, 0, 1]')
n = 1
print(f'output: {sol.sumZero(n)}, expected: [0]')
