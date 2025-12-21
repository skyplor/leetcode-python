class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        '''
        For a valid triangle, sum of 2 sides must be larger than 3rd side, i.e. a + b > c
        We can first sort the nums list, then we have a loop that goes through each number, setting that as `c`.
        Next, we use 2 pointers to find all valid pairs of `a` and `b` that is greater than `c`.
        '''

        nums.sort()
        result = 0
        n = len(nums)
        for c in range(n):
            a = 0
            b = c - 1
            while a < b:
                sum = nums[a] + nums[b]
                if sum <= nums[c]:
                    a += 1
                else:
                    # if the sum is greater, then all pairs from a, a+1... to b will work, so we need to get all triangles between b and a
                    result += b - a
                    b -= 1

        return result


sol = Solution()
print(f'output: {sol.triangleNumber([2, 2, 3, 4])}, expected: 3')
print(f'output: {sol.triangleNumber([4, 2, 3, 4])}, expected: 4')
