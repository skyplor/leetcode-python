class Solution:
    def minOperations(self, nums: list[int]) -> int:
        '''
        We will track the layers using a monotonic (non-decreasing) stack.
        We have a loop that goes through each num
            - In each iteration,
                - we recursively pop from stack while num < stack[-1]
                - if num != stack[-1]
                    - add 1 operation to result
                - push num onto stack
        '''
        stack = [0]
        res = 0
        for num in nums:
            while num < stack[-1]:
                stack.pop()
            if num != stack[-1]:
                res += 1
            stack.append(num)
            
        return res


sol = Solution()
# sol.minOperations([2, 0, 3, 4, 0, 5, 6])
# sol.minOperations([0, 3, 4, 0, 5, 0])
print(f'output: {sol.minOperations([0, 2])}, expected: 1')
print(f'output: {sol.minOperations([3, 1, 2, 1])}, expected: 3')
print(f'output: {sol.minOperations([1, 2, 1, 2, 1, 2])}, expected: 4')
