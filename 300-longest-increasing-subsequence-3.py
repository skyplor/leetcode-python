from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        This is an optimized version with Time Complexity of O(nlogn)
        The disadvantage of this is we WILL NOT BE ABLE to get the exact subsequence. We can only get the length
        We will maintain a list of increasing numbers. Each time we will either replace an element or extend the list
        if a number is larger than last element, we extend the list. 
        Otherwise, we use binary search to find the index where the number is greater than the previous index but smaller than current index,
        and we replace that value with this number
        '''
        n = len(nums)
        res = []

        for i in range(1, n):
            cur = nums[i]
            # find an element that is bigger than cur and the prev element is smaller than cur
            left = 0
            right = len(res)
            while left < right:
                mid = left + ((right - left) // 2)

                if cur > res[mid]:
                    left = mid + 1
                else:
                    right = mid
                        
            if left == len(res):
                res.append(cur)
            else:
                res[left] = cur
                        
        return len(res)
                


sol = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
output = sol.lengthOfLIS(nums)
print(f'nums: {nums}\noutput: {output}')
