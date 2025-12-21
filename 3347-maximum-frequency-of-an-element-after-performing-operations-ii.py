from collections import defaultdict

class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        '''
        This problem is similar to 3346 except the constraints. nums[i] and k can be larger now, from 10^5 changed to 10^9. We can use back the same OPTIMISED solution


        We can come up with a range of possible values at each nums index
            e.g. if nums[i] = 7 and k = 3, possible values: [4, 10]
            nums[i] - k <= t <= nums[i] + k

        Next, we can have a loop that goes through each possible `t` value, and check at each index, how many can reach that `t` value
            - At each index,
                - if nums[i] == t, then we don't need to decrement the numOperations as we no need to do any transformation
                - else, we need to decrement the numOperations
            - for a given target t, we can compute:
                - alreadyAt = count of elements already equal to t
                - canReach = count of elements that can be transformed to t (excluding those already at t)
            - We can have an equation for this as well:
                - maxFreq = alreadyAt + min(numOperations, canReach)

        Next, to determine the range of `t` to check:
            - it is definitely [min(nums) - k, max(nums) + k]
            - We might not even need to check through each value in this range. we can get the boundary values + nums[i] and just check those
            - {nums[i] - k , nums[i], nums[i] + k}

        We need to sort nums to ensure that our `t` moves in a single direction

        NOTE: This is an optimised version using line-sweep (3 pointers)
        For a target `t`, all elements in the range [t-k, t+k] can reach it
        '''
        nums.sort()
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        candidates_set = set()
        for num in nums:
            candidates_set.add(num - k)
            candidates_set.add(num)
            candidates_set.add(num + k)

        candidates = list(candidates_set)
        candidates.sort()

        max_freq = 0
        left = right = 0
        for t in candidates:
            while right < len(nums) and nums[right] <= t + k:
                right += 1

            while left < len(nums) and nums[left] < t - k:
                left += 1
            already_at = freq[t]
            total_in_range = right - left
            can_reach = total_in_range - already_at

            max_freq_at_t = already_at + min(numOperations, can_reach)
            if max_freq_at_t > max_freq:
                max_freq = max_freq_at_t

        return max_freq


sol = Solution()
nums = [1, 4, 5]
k = 1
numOperations = 2
print(f'Output: {sol.maxFrequency(nums, k, numOperations)}, expected: 2')
nums = [5, 11, 20, 20]
k = 5
numOperations = 1
print(f'Output: {sol.maxFrequency(nums, k, numOperations)}, expected: 2')
