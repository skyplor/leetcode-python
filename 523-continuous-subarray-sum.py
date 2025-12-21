from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        There is a brute force way which is to go through the loop twice and get ALL combinations, check against the `k` value.
        But this would be O(n²)
        
        The most efficient way is O(n).
        To achieve this, we will need a hashmap that stores the remainder as the key and the ending_index as the value
        We will have a loop that go through each number, each time we add the new number to the current total and then we get the remainder.
        If the remainder isn't in the hashmap, we add it in and continue.
        But if there is a remainder that already exists in the hashmap, that means from the end_index (that is stored in the hashmap) to the current index, the numbers within these 2 indices sums up to a multiple of k
        Why is this so?
            - e.g if a sum has a remainder of 5. Then we add somemore numbers and after some time, the remainder comes back to 5. That means we have gone through 1 round,
            - and all the numbers AFTER the initial index would have a sum that contributes to a multiple of k and so it's `5+0 = 5`
            - So since they contribute to `+0` that means we have a subarray.
            - Before returning, we also need to ensure that the subarray is of at least size 2. So we need to get the difference of the 2 indices (current_index - end_index_in_hash) and as long as it is >= 2, we can return True
            
        There is also an edge case that we need to handle. What if we add up a sum that has 0 as remainder? We can straight away return True, but how do we know that it is not a single value?
            - What we can do is to store this `0` in the hashmap right from the start so that we can re-use the logic above
            - But what would be the value of the ending_index?
            - We can store the ending_index as `-1` so that even if we get another remainder 0 when we get the first number, the size would be (0 - -1 = 1)
        '''
        
        remainder_hash = {0: -1} # handle edge case of first number that is a multiple of k
        total = 0
        
        for i, num in enumerate(nums):
            total += num
            remainder = total % k
            if remainder in remainder_hash:
                end_index = remainder_hash[remainder]
                if i - end_index >= 2:
                    return True
            else:
                remainder_hash[remainder] = i
                
        return False
        
    
sol = Solution()
nums = [23,2,4,6,7]
k = 6
print(f'output: {sol.checkSubarraySum(nums, k)}')
nums = [23,2,6,4,7]
k = 6
print(f'output: {sol.checkSubarraySum(nums, k)}')
nums = [23,2,6,4,7]
k = 13
print(f'output: {sol.checkSubarraySum(nums, k)}')