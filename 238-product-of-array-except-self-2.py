from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        This is an enhancement of the first solution by making it memory O(1) by storing the prefix and postfix directly in the output result
        we will loop through the nums once, each time we have a variable (cur_prefix) that stores the prefix product value up till i
          - we update the result[i] with the cur_prefix
          - we multiply the nums[i] with the cur_prefix and update cur_prefix to that new value
        we then loop through the nums in reversed order, each time we have a variable (cur_postfix) that stores the postfix product value up till i
          - we multiple the cur_postfix with the prefix value in result[i] and update result[i] to that value
          - we multiply the nums[i] with the cur_postfix and update cur_postfix to that new value
        '''
        n = len(nums)
        cur_prefix, cur_postfix = 1, 1
        result = [1]*n
        for i in range(n):
            result[i] = cur_prefix
            cur_prefix *= nums[i]

        for j in range(n-1, -1, -1):
            result[j] *= cur_postfix
            cur_postfix *= nums[j]

        return result


sol = Solution()
input = [1, 2, 3, 4]
print(f'Input: {input}\nOutput: {sol.productExceptSelf(input)}')
