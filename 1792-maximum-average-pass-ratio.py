from typing import List
from heapq import heappush, heappop


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        '''
        We need to greedily choose which class benefits most from adding a student. 
        The key insight: calculate the improvement in pass ratio for each class if we add one student.

        A brute force way would be to use backtracking and try all possible combinations to get the maximum. But if we have more than 1 extra students, the complexity will increase exponentially
        e.g we have 10^5 classes and if we go through it 2 times, it will be 10^10. We will hit TLE

        We will need to get the largest increase in pass ratio IF we add 1 student to it. We have a max_heap that return the next possible class based on the pass ratio
            - improvement = ((pass + 1) / (total + 1)) - (pass / total)
            - So we can store as a tuple of (improvement, pass, total) and the improvement has to be negated for it to be a max_heap
        
        At the end, we get all the pass and total values from the heap and calculate the pass ratio from there
        '''
        n = len(classes)
        max_heap = []

        def improvement(passes, total):
            return ((passes + 1) / (total + 1)) - (passes / total)

        for pass_qty, total_qty in classes:
            heappush(max_heap, (-improvement(pass_qty,
                     total_qty), pass_qty, total_qty))

        for _ in range(extraStudents):
            _, pass_qty, total_qty = heappop(max_heap)
            pass_qty += 1
            total_qty += 1

            heappush(max_heap, (-improvement(pass_qty, total_qty), pass_qty, total_qty))

        return sum(pass_qty / total_qty for _, pass_qty, total_qty in max_heap) / n


sol = Solution()
classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2
print(f'output: {sol.maxAverageRatio(classes, extraStudents)}')
