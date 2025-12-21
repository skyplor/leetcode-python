class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        '''
        We have 2 pointers that represent the starting.
        For each starting position, we move the pointer k times to check if it's strictly increasing.
            - If yes, return.
            - Else, once we reach one that has value smaller or equal to the previous value, we use that as the starting point instead
        '''
        start_first, start_second = 0, k
        n = len(nums)

        while start_second < n - k + 1:
            curr_first, curr_second = start_first + 1, start_second + 1
            found_ans = True
            while curr_first < start_first + k:
                curr_first_val, curr_second_val = nums[curr_first], nums[curr_second]
                prev_first_val, prev_second_val = nums[curr_first - 1], nums[curr_second - 1]
                if curr_first_val > prev_first_val and curr_second_val > prev_second_val:
                    curr_first += 1
                    curr_second += 1
                elif curr_first_val <= prev_first_val or curr_second_val <= prev_second_val:
                    found_ans = False
                    start_first = curr_first
                    start_second = curr_second
                    break
                
            if found_ans:
                return True
            
        return False
            
            
    
sol = Solution()
print(f'output: {sol.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3)}, expected: True')
print(f'output: {sol.hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7], 5)}, expected: False')
print(f'output: {sol.hasIncreasingSubarrays([-15, 19], 1)}, expected: True')
print(f'output: {sol.hasIncreasingSubarrays([5,8,-2,-1], 2)}, expected: True')