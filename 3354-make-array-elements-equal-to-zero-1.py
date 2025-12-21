class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        '''
        We just simulate the process
        '''
        
        def check_valid(numbers: list[int], pos: int, direction: int) -> bool:
            n = len(numbers)
            while 0 <= pos < n:
                if numbers[pos] != 0:
                    direction *= -1
                    numbers[pos] -= 1
                pos += direction
                
            return numbers.count(0) == n
            
        total = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                continue
            # left direction
            valid = check_valid(nums.copy(), i, -1)
            if valid:
                total += 1
            
            # right direction
            valid = check_valid(nums.copy(), i, 1)
            if valid:
                total += 1
                
        return total


sol = Solution()
print(f'output: {sol.countValidSelections([1, 0, 2, 0, 3])}, expected: 2')
print(
    f'output: {sol.countValidSelections([2, 3, 4, 0, 4, 1, 0])}, expected: 0')
