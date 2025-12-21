from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        '''
        We use an extra array and go through nums, then set the num into the temp and at the end copy the nums back
        To find the new_index to put, we just add current index by k, then mod by the length of nums
        '''
        n = len(nums)
        temp = [0] * n
        for i, num in enumerate(nums):
            new_index = (i + (k % n)) % n
            temp[new_index] = num
            
        print(temp)
        for i, num in enumerate(temp):
            nums[i] = num
        
        return nums


sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(f'output: {sol.rotate(nums, k)}')
