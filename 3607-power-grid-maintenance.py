from collections import defaultdict
from heapq import heapify, heappop


class Solution:
    def processQueries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
        '''
        We can have an offline set
        We need to preprocess to build a hashmap of station:min_heaps
        We will use DSU and build the parent list. The idea behind this is if the stations share the same root parent, that means they are all connected to each other.
        So we can run another loop that build a list of stations connected to the same parent e.g {parent: [station1, station2,...]}
        And we build the grid after that by going through each station, get the parent of that station, get the list of stations connected to this parent and add all into the min_heap
        If the query is a check, then we just check if the station is in the offline set.
            - If no, we return station
            - If yes, we go through the priority queue and get the first item off the queue. we have a while loop that will dequeue if the min station is offline
        '''
        offline = set()
        parent = [i for i in range(c+1)]
        rank = [1 for _ in range(c+1)]

        def union(i, j):
            nonlocal parent, rank

            parent_i, parent_j = find(i), find(j)
            if parent_i == parent_j:
                return

            if rank[parent_i] < rank[parent_j]:
                parent[parent_i] = parent[parent_j]
                rank[parent_j] += rank[parent_i]
            else:
                parent[parent_j] = parent[parent_i]
                rank[parent_i] += rank[parent_j]

        def find(i):
            nonlocal parent

            if parent[i] == i:
                return i
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return parent[i]


        for s1, s2 in connections:
            union(s1, s2)

        connected_components = defaultdict(list)
        for i in range(1, len(parent)):
            connected_components[find(i)].append(i)

        for v in connected_components.values():
            heapify(v)
            
        component_root = {}
        for k, v in connected_components.items():
            for s in v:
                component_root[s] = k

        res = []
        for type, station in queries:
            if type == 2:
                offline.add(station)
                continue

            connections = connected_components[component_root[station]]

            if station not in offline:
                res.append(station)
                continue

            while connections and ((connections[0] in offline) or (connections[0] == station)):
                heappop(connections)

            if connections:
                res.append(connections[0])
            else:
                res.append(-1)

        return res


sol = Solution()
# c = 5
# connections = [[1, 2], [2, 3], [3, 4], [4, 5]]
# queries = [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]
# print(
#     f'output: {sol.processQueries(c, connections, queries)}, expected: [3, 2, 3]')

# c = 3
# connections = []
# queries = [[1, 1], [2, 1], [1, 1]]
# print(
#     f'output: {sol.processQueries(c, connections, queries)}, expected: [1, -1]')

c = 4
connections = [[3, 1], [2, 4], [2, 1], [1, 4]]
queries = [[2, 3], [2, 1], [1, 1], [1, 3], [2, 2], [2, 1], [
    1, 2], [2, 3], [1, 4], [2, 2], [1, 1], [2, 2], [2, 1], [2, 2]]
print(
    f'output: {sol.processQueries(c, connections, queries)}, expected: [2,2,4,4,4]')
