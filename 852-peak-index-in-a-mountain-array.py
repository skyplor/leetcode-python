class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        '''
        Using binary search, we check the mid value, mid - 1 and mid + 1.
        if it is increasing (i.e mid > mid - 1 and mid + 1 > mid), then we search right by setting left = mid + 1
        if it is decreasing (i.e mid < mid - 1 and mid + 1 < mid), then we search left by setting right = mid
        otherwise, we have found the peak index and return mid
        '''
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            # increasing
            if arr[mid + 1] > arr[mid]:
                left = mid + 1
            # decreasing
            else:
                right = mid

        return left


sol = Solution()
# arr = [0, 1, 0]
# arr = [0, 2, 1, 0]
# arr = [0, 5, 10, 2]
arr = [0, 3, 5, 12, 2]
output = sol.peakIndexInMountainArray(arr)
print(f'output: {output}')
