from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Brute force: O(n+m)
          - merge both arrays then take the medium 2 indices

        Efficient: O(log (n+m))
        We can try to use binary search whenever we see O(log...)
        To get the median, we will need to know the left and right partitions
        Then we calculate how many items are there for each partition, e.g if total len = 13, then it will be 6 items on the left and right. Same for if total len = 12 i.e n//2
        Next, picking one of the nums, preferably the one of a smaller length. We have a `left` and `right` pointer that point to index 0 and len - 1 
        We then get the `mid` point of it. We calculate how many items are there from left pointer to mid pointer (inclusive). This forms a temp left_partition.
        From this left_partition, we calculate how many more items we need to get from the other nums array using (6 - len(temp_left_partition)) and this will form the remainder of the temp left_partition
        Next, we need to check if the temp left partitions we have chosen are valid.
            - all elements in first nums array must be smaller than the remaining right partition of the second nums array
            - all elements in second nums array must be smaller than the remaining right partition of the first nums array
            - So we compare the right most item of the temp left partition of first nums against the left most item of the right partition of the second nums array
                - If the value of left partition item is smaller, we have passed the first rule
            - and compare the the right most item of the temp left partition of second nums against the left most item of the right partition of the first nums array
                - If the value of left partition item is smaller, we have passed the second rule
        If valid, then depending on whether the total length is even or odd:
            - if even, we need to get 1 item from left partition and 1 item from right partition
                - median = (max(nums_1_left_partition[-1], nums_2_left_partition[-1]) + min(nums_1_right_partition[0], nums_2_right_partition[0])) / 2
            - if odd, we just need to get 1 item from the right partition
                - median = min(nums_1_right_partition[0], nums_2_right_partition[0])
        If not valid, then depending on which rule is failing
            - If first rule is failing, i.e nums_1_left_partition's last item is bigger than nums_2_right_partition's first item
                - then we need to increase nums_2 proportion of items in the left partition
                - this means we need to run binary search on the nums 2 by shifting `left` pointer to `mid`+1 and recalculating the `mid` from there
            - Otherwise,
                - we need to increase nums_1 proportion of items and we shift `right` pointer to `mid` and recalculating the `mid` from there
        '''
        small_nums = nums1
        big_nums = nums2
        if len(nums2) < len(nums1):
            small_nums, big_nums = big_nums, small_nums

        small_nums_len = len(small_nums)
        big_nums_len = len(big_nums)
        total_len = small_nums_len + big_nums_len
        left_len = total_len // 2
        left, right = 0, small_nums_len
        while left <= right:
            mid = left + ((right - left) // 2)
            max_small_left = small_nums[mid-1] if mid > 0 else float('-inf')
            min_small_right = small_nums[mid] if mid < small_nums_len else float('inf')
            big_left_len = left_len - mid
            max_big_left = big_nums[big_left_len-1] if big_left_len > 0 else float('-inf')
            min_big_right = big_nums[big_left_len] if big_left_len < big_nums_len else float('inf')
            if max_small_left <= min_big_right and max_big_left <= min_small_right:
                if total_len % 2 == 0:
                    median = (max(max_small_left, max_big_left) + min(min_small_right, min_big_right)) / 2
                else:
                    median = min(min_small_right, min_big_right)
                    
                return median
            
            if max_small_left > min_big_right:
                # reduce temp_small_left size, so shift right pointer
                right = mid - 1
            else:
                # increase temp_small_left size, so shift left pointer
                left = mid + 1
            
            


sol = Solution()
nums1 = [1, 3]
nums2 = [2, 4, 5]
output = sol.findMedianSortedArrays(nums1, nums2)
print(f'nums1: {nums1}\nnums2: {nums2}\noutput: {output}')
