class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        '''
        We will have a left and right pointer and a hashset that contains all the nums seen so far within the left and right section
        We start off from index 0. If a num wasn't seen before, add it into the `seen` hashset. We also maintain a result var that stores the maximum value.
        We will also have a temp result var that store the current total sum. We will add into this temp result var  if a num wasn't seen before, and then compare that temp with the result.
        If this temp result is higher than result, update result
        If we encounter a num that was seen before, we remove the number pointed to by the left pointer, and also subtract from temp result and then move left pointer forward.
        We continue with this in a while loop with the condition that the num pointed by the left pointer != number pointed by the right pointer
        '''
        seen = set()
        result = 0
        temp_result = 0
        left = 0
        for right, right_num in enumerate(nums):
            if right_num not in seen:
                seen.add(right_num)
                temp_result += right_num
                result = max(result, temp_result)
                continue

            while nums[left] != right_num and left < right:
                left_num = nums[left]
                seen.remove(left_num)
                temp_result -= left_num
                left += 1
            left += 1

        return result


sol = Solution()
# nums = [4, 2, 4, 5, 6]
nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
output = sol.maximumUniqueSubarray(nums)
print(f'output: {output}')
