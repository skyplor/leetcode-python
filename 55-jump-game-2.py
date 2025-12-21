class Solution:
    def canJump(self, nums: list[int]) -> bool:
        '''
        Using 2-pointer approach, we can have a pointer `target` that starts at the last index, and another pointer `start` that will continuously move from last index to start of array
        Logic:
            - we will have the `start` pointer be at n-2 index.
            - If it is possible to go from n-2 to target, i.e nums[start] + start >= target,
            - then we can reduce the problem to check if we can reach `start` pointer.
            - So `target` will move to `start` and `start` = `start` - 1
            
        this loop will happen until `start` < 0
        once we exit from loop, if target is not at 0, then we can't reach
        '''
        target = len(nums) - 1
        start = target - 1
        while start >= 0:
            if nums[start] + start >= target:
                target = start

            start -= 1
            
        return target == 0
    
sol = Solution()
nums = [2,3,1,1,4]
output = sol.canJump(nums)
print(f'output: {output}')