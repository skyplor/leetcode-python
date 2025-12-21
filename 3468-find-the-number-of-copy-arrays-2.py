class Solution:
    def countArrays(self, original: list[int], bounds: list[list[int]]) -> int:
        '''
        We need to be able to count how many arrays we can create while adhering to the following rules:
            - the difference between each adjacent value of the copied array has to be the same as the original array's
            - each element of the copied array has to be bounded to the corresponding lo and hi values of the same index as stated in `bounds`

        We can compute the interval for each position, then add it into the corresponding bounds.
        Then we check if the new bound intersects with the next bound.
        If it intersects, we get the intersection values and continue to the next index
        This way we only compute for 2 numbers instead of simulating the actual arrays.
        At the end, we calculate how many numbers are there in the final intersection and that is the result
        '''

        lo, hi = bounds[0]

        for i in range(1, len(bounds)):
            bound_lo, bound_hi = bounds[i]
            increment = original[i] - original[i-1]
            lo += increment
            hi += increment
            if bound_lo > hi:
                return 0
            if bound_lo > lo:
                lo = bound_lo
            if bound_hi < hi:
                hi = bound_hi
                
        if lo <= hi:
            return hi - lo + 1
        
        return 0


sol = Solution()
print(
    f'output: {sol.countArrays([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4], [4, 5]])} expected: 2')
