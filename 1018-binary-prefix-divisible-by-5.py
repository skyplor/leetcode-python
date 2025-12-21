class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        '''
        We have a loop that goes through each num, at each loop, we shift the bits by 1 to the left and OR with the num
        Next, get the result and mod 5 and store the result in a res array
        '''
        res = []
        cur = 0
        for num in nums:
            cur <<= 1
            cur |= num
            res.append(cur % 5 == 0)

        return res


sol = Solution()
print(
    f'output: {sol.prefixesDivBy5([0, 1, 1])}, expected: [True, False, False]')
print(
    f'output: {sol.prefixesDivBy5([1, 1, 1])}, expected: [False, False, False]')
print(
    f'output: {sol.prefixesDivBy5([0, 1, 1, 1, 1, 1])}, expected: [True, False, False, False, True, False]')
