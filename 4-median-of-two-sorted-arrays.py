from typing import List

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # get the total len of both nums, divide by half to get the left partition
    # get the mid of nums1 and use the left partition of nums1 as the base
    # get the remaining of nums2 after deducting the length of left partition of nums1
    # compare the last element of nums1-left-partition with first element of nums2-right-partition, ensure it is less than or equal to nums2-right-partition
    # compare the last element of nums2-left-partition with first element of nums1-right-partition, ensure it is less than or equal to nums1-right-partition
    # if nums2 is not less than, then we need to reduce nums2, increase nums1, so we increment the l pointer
    # if nums1 is not less than, then we need to reduce nums1, so we decrement the r pointer
    # once we get the correct left partition, we just need to know if total length of both is even or odd.
    # if even, we get the next smallest element from both and divide by 2
    #   get the max of nums1 and nums2 left partition and min of nums1 and nums2 right partition and divide by 2
    # if odd, we get the next smallest element from either nums1 or nums2
    
    A, B = nums1, nums2
    if len(B) < len(A):
      A, B = B, A
    total = len(nums1) + len(nums2)
    half = total // 2
    l, r = 0, len(A) - 1
    
    while True:
      i = l + (r - l) // 2
      j = half - i - 2
      A_left = A[i] if i >= 0 else float("-infinity")
      A_right = A[i + 1] if (i + 1) < len(A) else float("infinity")
      B_left = B[j] if j >= 0 else float("-infinity")
      B_right = B[j + 1] if (j + 1) < len(B) else float("infinity")
      if A_left <= B_right and B_left <= A_right:
        if total % 2:
          return min(A_right, B_right)

        return (max(A_left, B_left) + min(A_right, B_right)) / 2
      elif A_left > B_right:
        r = i - 1
      else:
        l = i + 1
    
sol = Solution()
nums1 = [1, 3]
nums2 = [2, 4, 5]
output = sol.findMedianSortedArrays(nums1, nums2)
print(f'nums1: {nums1}\nnums2: {nums2}\noutput: {output}')