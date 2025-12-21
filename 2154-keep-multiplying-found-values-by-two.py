class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        '''
        We go through list of nums, add all into a set
        Next, we have a loop that search for the original in the set and if found, multiply by 2 and check again
        '''
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        for _ in range(len(nums) + 1):
            if original not in nums_set:
                break
            original *= 2

        return original


sol = Solution()
print(
    f'output: {sol.findFinalValue(nums=[5, 3, 6, 1, 12], original=3)}, expected: 24')
print(f'output: {sol.findFinalValue(nums=[2, 7, 9], original=4)}, expected: 4')
print(f'output: {sol.findFinalValue(nums=[4], original=4)}, expected: 8')
print(f'output: {sol.findFinalValue(nums=[17,2,3,20,4,10,1], original=2)}, expected: 8')
print(
    f'output: {sol.findFinalValue(nums=[1, 16, 13, 19, 12, 10], original=2)}, expected: 2')
print(f'output: {sol.findFinalValue(nums=[2,7,9], original=4)}, expected: 4')
