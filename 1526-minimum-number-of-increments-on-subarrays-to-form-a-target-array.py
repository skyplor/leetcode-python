class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        '''
        We can use Greedy approach for this.
        We will have a `res` to keep track of number of operations
        We go through each element,
            - if the element is bigger than prev element, we add the difference to the `res`
            - if smaller, we don't do anything
        '''
        res = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                res += target[i] - target[i - 1]
        
        return res
        

sol = Solution()
print(f'output: {sol.minNumberOperations([1, 2, 3, 2, 1])}, expected: 3')
print(f'output: {sol.minNumberOperations([3, 1, 1, 2])}, expected: 4')
print(f'output: {sol.minNumberOperations([3, 1, 5, 4, 2])}, expected: 7')
