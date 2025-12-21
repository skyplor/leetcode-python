from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Since we can't do division, one way is to get the product of every items BEFORE this index and the product of every items AFTER this index
        we can calculate this in O(n) time by iterating through the list and computing prefix and postfix product values
        '''
        n = len(nums)
        prefix, postfix = [1]*n, [1]*n
        for i in range(n):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1] * nums[i]

        for j in range(n - 1, -1, -1):
            if j == n-1:
                postfix[j] = nums[j]
            else:
                postfix[j] = postfix[j+1] * nums[j]

        result = []
        for k in range(n):
            prefix_product = prefix[k - 1] if k > 0 else 1
            postfix_product = postfix[k + 1] if k < n - 1 else 1
            result.append(prefix_product * postfix_product)

        return result


sol = Solution()
nums = [1, 2, 4, 6]
output = sol.productExceptSelf(nums)
print(f'output: {output}')
