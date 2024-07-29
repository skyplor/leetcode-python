from typing import List
import random

class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:
    '''
    Using quick sort

    1. Choose a pivot: In this implementation, we always choose the last element of the current subarray as the pivot.

    2. Partitioning: We rearrange the elements in the subarray so that all elements smaller than or equal to the pivot come before it, and all elements greater than the pivot come after it. This is done as follows:
        - We use two pointers: i (slow pointer) and j (fast pointer).
        - i keeps track of where we should place the next element that's smaller than or equal to the pivot.
        - We iterate through the subarray with j.
        - Whenever we find an element at j that's smaller than or equal to the pivot, we swap it with the element at index i and increment i.
        - After this process, i points to the correct final position for the pivot.

    3. Place the pivot: We swap the pivot (which is at the end of the subarray) with the element at position i. Now the pivot is in its correct sorted position.

    4. Recursive calls: We recursively apply this process to the two subarrays on either side of the pivot:
        - The left subarray (elements smaller than or equal to the pivot)
        - The right subarray (elements greater than the pivot)

    5. Base case: If a subarray has 0 or 1 element (i.e., head >= tail), we don't need to do anything, so we just return.
    '''

    def quick_sort(head, tail):
      if head >= tail:
        return

      pivot = random.randint(head, tail)
      nums[pivot], nums[tail] = nums[tail], nums[pivot]
      pivot_val = nums[tail]
      left, right = head, tail - 1
      i = left
      
      while i <= right:
        if nums[i] < pivot_val:
          nums[left], nums[i] = nums[i], nums[left]
          left += 1
          i += 1
        elif nums[i] > pivot_val:
          nums[right], nums[i] = nums[i], nums[right]
          right -= 1
        else:
          i += 1

      nums[left], nums[tail] = nums[tail], nums[left]

      quick_sort(head, left - 1)
      quick_sort(right + 1, tail)

    quick_sort(0, len(nums) - 1)
    return nums

sol = Solution()
nums = [5,2,3,1]
print(f'output: {sol.sortArray(nums)}')