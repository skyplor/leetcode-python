from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        We use a sliding window to find the longest subarray of 1s after deleting one element.
        We use a left pointer to keep track of the start of the window and a right pointer to keep track of the end of the window.
        We use a zero_idx to keep track of the index of the last zero we saw.
        We use a max_len to keep track of the longest subarray of 1s we have seen.
        We use a cur_len to keep track of the current length of the subarray of 1s.
        Time: O(n)
        Space: O(1)
        '''
        zero_idx = -1
        left = 0
        max_len = 0
        cur_len = 0
        for right in range(0, len(nums)):
            if nums[right] == 0:
                if zero_idx == -1:
                    zero_idx = right
                else:
                    left = zero_idx + 1
                    zero_idx = right

                cur_len = right - left  # we don't +1 here to exclude the zero
                max_len = max(max_len, cur_len)
            else:
                cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len if max_len < len(nums) else max_len - 1
