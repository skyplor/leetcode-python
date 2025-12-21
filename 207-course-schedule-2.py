from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        We have a hash map of prerequisites
        We also have a done and a visiting set
        We use dfs so each time we check the node's status:
            if node is done, we can return True
            if node is in visiting, that means cycle detected, return False
            Then we mark the node as visiting
            We check through the prerequisites and use dfs for each prerequisite
            We return False immediately if any prerequisite fails
            Then we remove the node from visiting and add it into done and return True
        We also need to go through the numCourses to make sure we don't miss out any separated node and run dfs on each
        '''
        prerequisite_hash = {i: [] for i in range(numCourses)}
        visiting = set()
        done = set()

        def dfs(node: int) -> bool:
            if node in done:
                return True
            if node in visiting:
                return False

            prerequisite_list = prerequisite_hash[node]
            visiting.add(node)

            for prerequisite in prerequisite_list:
                if not dfs(prerequisite):
                    return False

            visiting.remove(node)
            done.add(node)
            return True

        for node, prerequisite in prerequisites:
            prerequisite_hash[prerequisite].append(node)

        for node in range(numCourses):
            if node in done:
                continue
            if not dfs(node):
                return False

        return True


sol = Solution()
numCourses = 2
prerequisites = [[1, 0]]
# prerequisites = [[1, 0], [0, 1]]
# prerequisites = [[1, 0], [2, 1], [3, 1]]
output = sol.canFinish(numCourses, prerequisites)
print(f'output: {output}')
