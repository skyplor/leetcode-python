class Solution:
    def countArrays(self, original: list[int], bounds: list[list[int]]) -> int:
        '''
        We need to be able to count how many arrays we can create while adhering to the following rules:
            - the difference between each adjacent value of the copied array has to be the same as the original array's
            - each element of the copied array has to be bounded to the corresponding lo and hi values of the same index as stated in `bounds`

        we have a loop, and make use of the first index of the bounds array. Looping through each number, we then try to increment by getting the increment value from original array.
        Then we see if the value of the next index after incrementing fits within the bound of the corresponding index, and we proceed all the way until we hit n-1.
        Once that is reached, we are sure that this array is good to go and we can add 1 to the result
        then we proceed to the next number
        
        This way is fine, but its performance is not good. Will encounter TLE if initial range is huge.
        '''

        n = len(original)
        initial_lo, initial_hi = bounds[0]
        res = 0
        for initial_num in range(initial_lo, initial_hi + 1):
            i = 0
            num = initial_num
            while i < len(original) - 1 and bounds[i][0] <= num <= bounds[i][1]:
                increment_val = original[i+1] - original[i]
                num += increment_val
                i += 1
            if i != len(original) - 1 or not bounds[i][0] <= num <= bounds[i][1]:
                continue
            res += 1
        return res


sol = Solution()
print(
    f'output: {sol.countArrays([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4], [4, 5]])} expected: 2')
