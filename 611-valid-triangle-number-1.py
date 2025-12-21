import bisect


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        '''
        For a valid triangle, sum of 2 sides must be larger than 3rd side, i.e. a + b > c
        We can first sort the nums list, then go through each pair of nums using 2 for loops and with each pair,
            we try to binary search the rest of the numbers to find the largest idx that is smaller than the sum of the 2 numbers

        e.g [2, 2, 3, 4]
        a = 2, b = 2
        binary search will start at j+1 to end of array, and returns index 2. We only need to consider from second number to this index, so it's j+1 to index 2. Since `j` is 1, so there's only 1 number smaller.
        Add 1 to the result
        next, a = 2 (at idx = 0), b = 3 (at idx = 2)
        binary search returns 3, so 1 number.
        Add 1 to the result
        next, a = 2 (at idx = 0), b = 4
        binary search returns -1, so no numbers
        next, a = 2 (at idx = 1), b = 3 (at idx = 2)
        binary search returns 3, so 1 number.
        Add 1 to the result
        next, a = 2 (at idx = 1), b = 4
        binary search returns -1, so no numbers
        next, a = 3 (at idx = 2), b = 4
        binary search returns -1, so no numbers

        we have reached the end and result = 3

        e.g 2 [4, 2, 3, 4]
        sorted = [2, 3, 4, 4]
        a = 2, b = 3
        binary search will start at j+1 to end of array, and returns index 3. We only need to consider from second number to this index, so it's j+1 to index 3. Since `j` is 1, so there are 2 numbers smaller.
        Add 2 to the result
        next, a = 2 (at idx = 0), b = 4 (at idx = 2)
        binary search returns 3, so 1 number.
        Add 1 to the result
        next, a = 2 (at idx = 0), b = 4 (at idx = 3)
        binary search returns -1, so no numbers
        next, a = 3 (at idx = 1), b = 4 (at idx = 2)
        binary search returns 3, so 1 number.
        Add 1 to the result
        next, a = 3 (at idx = 1), b = 4 (at idx = 3)
        binary search returns -1, so no numbers
        next, a = 4 (at idx = 2), b = 4 (at idx = 3)
        binary search returns -1, so no numbers

        we have reached the end and result = 4
        '''

        def binary_search(left, right, target):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return right

        nums.sort()
        result = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                largest_idx = binary_search(j+1, n, nums[i] + nums[j])
                # largest_idx = bisect.bisect_left(nums, nums[i] + nums[j], j+1)
                result += largest_idx - j - 1

        return result


sol = Solution()
print(f'output: {sol.triangleNumber([2, 2, 3, 4])}, expected: 3')
print(f'output: {sol.triangleNumber([4, 2, 3, 4])}, expected: 4')
