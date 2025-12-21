class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        '''
        For a valid triangle, length of 2 sides must be greater than length of the 3rd side
        We first sort the nums, then we have a loop that goes from i = 0 to n, and the index will represent the 3rd side.
            - At the same time, we take sum of the values pointed at indices n-1 and n-2
            - If the values are valid, then we get the max_parameter
        '''
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a = nums[i+2]
            b = nums[i+1]
            c = nums[i]
            if a + b > c:
                return a+b+c
            
        return 0


sol = Solution()
print(f'output: {sol.largestPerimeter([2, 1, 2])}, expected: 5')
print(f'output: {sol.largestPerimeter([1, 2, 1, 10])}, expected: 0')
