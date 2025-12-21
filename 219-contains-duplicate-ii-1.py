class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        '''
        Using a hashmap, we go through each num, if num doesn't exist in hash, add it as a key and the index as value
        if num exist in hash, compare and check the index. If abs(i-j) <= k, return true. else, we replace the stored value with current index
        '''
        hash = {}
        for i, num in enumerate(nums):
            if num not in hash:
                hash[num] = i
            else:
                stored_index = hash[num]
                if abs(i - stored_index) <= k:
                    return True
                hash[num] = i
        
        return False
    
sol = Solution()
nums = [1,2,3,1]
k = 3
output = sol.containsNearbyDuplicate(nums, k)
print(f'output: {output}')