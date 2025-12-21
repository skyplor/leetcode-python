class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        '''
        We can get the total of the nums and get the remainder when mod by `k`.
        This would be the number of operations needed
        '''
        return sum(nums) % k
        
sol = Solution()
print(f'output: {sol.minOperations(nums = [3,9,7], k = 5)}, expected: 4')
print(f'output: {sol.minOperations(nums = [4,1,3], k = 4)}, expected: 0')
print(f'output: {sol.minOperations( nums = [3,2], k = 6)}, expected: 5')