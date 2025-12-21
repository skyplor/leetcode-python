from typing import List

class Solution:
    def max_value(self, weights: List[int], values: List[int], max_weight: int) -> int:
        '''
        3 rules of DP:
            1. Express in terms of index. In this case, at each index, we have a bag capacity W so `dp(idx, W)`
            2. Explore all possibilities (pick vs no-pick)
            3. Get the max of all possibilities
            
        At each index, we can either take the item or don't take the item. Then we continue to explore the next index
        We use recursion for this and pass in the index and max_weight
        '''

        def get_max(i, wt):
            if i == 0:
                if weights[0] <= wt:
                    return values[0]
                return 0

            # don't take
            dont_take_value = get_max(i-1, wt)
            take_value = float('-inf')
            if weights[i] <= wt:
                take_value = values[i] + get_max(i-1, wt-weights[i])
                
            return max(dont_take_value, take_value)
            
        return get_max(2, max_weight)
    
sol = Solution()
weights = [10,20,30]
values = [60,100,120]
max_weight = 50
print(f'output: {sol.max_value(weights, values, max_weight)}')
weights = [1,2,3]
values = [10,20,30]
max_weight = 5
print(f'output: {sol.max_value(weights, values, max_weight)}')