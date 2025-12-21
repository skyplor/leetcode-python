from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        We have a hash of adjacency list
        We have a done set
        we also maintain a hash of in-degrees count for each node
        We then use a queue and add each of those nodes with in-degrees == 0 into the queue
        in the queue, we get the left most item, and add this item into the done set. We then reduce all in-degrees of each neighbour by 1 to represent we have complete the prerequisite
        if the neighbour's indegree is now 0, then we add this neighbour into the queue as well
        at the end, if length of done is not equal to the numCourses, that means a loop exist and we won't be able to finish
        '''
        adj_list = {i: [] for i in range(numCourses)}
        done = set()
        indegrees = {i: 0 for i in range(numCourses)}
        queue = deque()

        for node, prerequisite in prerequisites:
            adj_list[prerequisite].append(node)
            indegrees[node] += 1

        for node in indegrees:
            indegree = indegrees[node]
            if indegree == 0:
                queue.append(node)

        while queue:
            cur = queue.popleft()
            done.add(cur)
            for next_course in adj_list[cur]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    queue.append(next_course)

        return len(done) == numCourses


sol = Solution()
numCourses = 2
prerequisites = [[1, 0]]
# prerequisites = [[1, 0], [0, 1]]
# prerequisites = [[1, 0], [2, 1], [3, 1]]
output = sol.canFinish(numCourses, prerequisites)
print(f'output: {output}')
