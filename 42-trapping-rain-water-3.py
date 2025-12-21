from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        To know how much water can be trapped, we need to get the min(max_left, max_right)
        Then, using that we subtract from the current height to know how much water can be trapped
            res += min(max_left, max_right) - h[i]
        To know the max_left and max_right, we can use 2-pointer approach
        start from index 0 for left, last index for right
        We have a while loop with condition left < right
            at each point, we decide if we want to shift left or right. we shift the one that is the smaller of the two (max_left vs max_right)
            if we are going to shift max_left, that means max_left is the determining factor (based on the equation of `min(max_left, max_right) - h[i])`, so at this point, before shifting the corresponding pointer (left or right), we will calculate the amount of water trapped (max_left - h[left]) and add into res
            if both max heights are the same, it doesn't matter and we can default to shifting left
            we also need to update the max_heights before moving the pointer
        '''
        res = 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        while left < right:
            if max_left <= max_right:
                res += max(0, max_left - height[left])
                max_left = max(max_left, height[left])
                left += 1
            else:
                res += max(0, max_right - height[right])
                max_right = max(max_right, height[right])
                right -= 1

        return res


sol = Solution()
input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
output = sol.trap(input)
print(f'Input: {input}\nOutput: {output}')
