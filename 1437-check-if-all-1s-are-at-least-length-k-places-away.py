class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        '''
        We go through each num, using a `prev` variable, if it is a `1`, and `current - prev - 1` isn't at least `k` return False
        '''
        prev = float('-inf')
        for i, num in enumerate(nums):
            if not num:
                continue

            if i - prev - 1 < k:
                return False
            prev = i

        return True


sol = Solution()
print(
    f'output: {sol.kLengthApart(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2)}, expected: True')
print(
    f'output: {sol.kLengthApart(nums=[1, 0, 0, 1, 0, 1], k=2)}, expected: False')
