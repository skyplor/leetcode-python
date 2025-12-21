from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        Using quick sort
        
        To reduce TLE error, we need to handle these 2 special cases:
            1. If array was already sorted, consistently choose the last element as the pivot will result in O(n²). So we use random index
            2. If there are duplicated elements, we should skip over instead of doing the swap
        '''

        def partition(low, high):
            # Randomly choose pivot and swap with last element
            random_idx = random.randint(low, high)
            nums[random_idx], nums[high] = nums[high], nums[random_idx]

            pivot = nums[high]
            
            # Three pointers: lt (less than), gt(greater than), i (current)
            lt = low
            gt = high
            i = low
            while i <= gt:
                if nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    i += 1
                    lt += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            return lt, gt

        def quick_sort(low, high):
            if low < high:
                lt, gt = partition(low, high)
                quick_sort(low, lt - 1)
                quick_sort(gt + 1, high)

        quick_sort(0, len(nums) - 1)
        return nums


sol = Solution()
nums = [5, 2, 3, 1]
print(f'output: {sol.sortArray(nums)}')
