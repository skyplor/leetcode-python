class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        '''
        Using a set, we will maintain a list of seen nums. After we add a num into the set, we check the size of the set and if it is greater than k, we remove the num that is outside of the window (nums[index - k])
        in each loop, we check if the current num exists in the set. if yes, we return True. Otherwise, we add the num in and remove existing num from the set if size is > k
        '''
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True

            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k])
        
        return False
    
sol = Solution()
nums = [1,2,3,1]
k = 3
output = sol.containsNearbyDuplicate(nums, k)
print(f'output: {output}')