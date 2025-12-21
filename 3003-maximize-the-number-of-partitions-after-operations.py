from functools import cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        '''
        We can use bitmasking for this problem
        At each index of the string, we have 2 choices
            - do not change the character
            - change character
            
        We can use 3 variables to keep track of the state at each iteration
            1. mask - the masking bits (a 26-bit that represents each of the characters in the alphabet, with "a" = 0th bit, "z" = 25th bit)
            2. changed - a flag stating whether we have changed the character in previous index. if it is false, that means we need to consider both scenarios (to change or don't change). But if it's true, that means we only need to consider don't change scenario
            3. index - what is the next index to process
            
        We can use recursion to process all possible scenarios, and have the base case as i == n, which we will then return 1 because if we reached end of the string, we will need to consider this last part as 1 partition

        At each iteration,
            - depending on which scenario/choice
                - If we are NOT changing,
                    - we get the character pointed by the index
                    - we create a temp variable by setting the bit for that character
                    - we OR this temp variable with the current mask state
                    - we check if the number of bits that are set > k
                        - if yes,
                            - add 1 to the result (we need to track the maximum partition discovered so far)
                            - change the current mask state to the temp variable to reset it to just this character
                - If we are changing,
                    - we try with another character (how do we try with another character?)
                        - we have a for loop of length 26
                            - at each iteration,
                                - if i == the current character, continue
                                - else
                                    - we do bit shift of 1 for i number of times
                                    - update the change flag to True
                                    - do the same steps as the above
        '''
        
        @cache
        def dp(mask, change, i):
            if i == len(s):
                return 1
            
            max_partitions = 0

            curr = ord(s[i]) - ord('a')
            curr_mask = 1 << curr
            new_mask = mask | curr_mask
            if new_mask.bit_count() <= k:
                max_partitions = max(max_partitions, dp(new_mask, change, i + 1))
            else:
                max_partitions = max(max_partitions, dp(curr_mask, change, i + 1) + 1)
                
            if not change:
                for j in range(26):
                    if j == curr: continue
                    curr_mask = 1 << j
                    new_mask = mask | curr_mask
                    if new_mask.bit_count() <= k:
                        max_partitions = max(max_partitions, dp(new_mask, True, i + 1))
                    else:
                        max_partitions = max(max_partitions, dp(curr_mask, True, i + 1) + 1)
                        
            return max_partitions
        
        return dp(0, False, 0)


sol = Solution()
print(f'output: {sol.maxPartitionsAfterOperations("accca", 2)}, expected: 3')
print(f'output: {sol.maxPartitionsAfterOperations("aabaab", 3)}, expected: 1')
print(f'output: {sol.maxPartitionsAfterOperations("xxyz", 1)}, expected: 4')
