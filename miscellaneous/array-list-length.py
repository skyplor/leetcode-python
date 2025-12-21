from typing import List


class Solution:
    '''
    https://app.codility.com/demo/results/trainingE9FYUH-DUR/
    '''
    def get_length(self, arr: List[int]):
        res = 0
        cur = 0
        while cur != -1:
            cur = arr[cur]
            res += 1

        return res

sol = Solution()
arr = [1,4,-1,3,2]
output = sol.get_length(arr)
print(f'output: {output}')