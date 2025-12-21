from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        we have 2 pointers which stores the 1st (small) and 2nd number (mid) in the sequence.
        we go through each element in nums
          - if the number is greater than the mid, then we have determined there's at least 1 subsequence that satisfy and can return True
          - if the number is between small and mid, then we can update mid since we want to reduce the distance between small and mid so that there's more chances of another number higher than mid IF mid is smaller
          - if number is smaller than small, then we can update small. We don't have to update mid because the mid belongs to another subsequence so if we have another number bigger than mid, that particular subsequence would be valid.
        '''
        small, mid = float('inf'), float('inf')
        for num in nums:
            if num > mid:
                return True
            if num <= small:
                small = num
            else:
                mid = num

        return False


sol = Solution()
nums = [1, 2, 3, 4, 5]
output = sol.increasingTriplet(nums)
print(f'output: {output}')
