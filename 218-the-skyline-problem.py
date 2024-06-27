from typing import List
from heapq import heappush, heappop


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        '''
        since the heap in python by default is a minheap and for this problem we are looking to have access
        to the maximum element we sort the heap based on the negative height.
        we define two series of events, starting event and end events. Each event contains
        left of the building, height of the building and right of the building. so the end events
        have 0 height and the ending position can also be 0 (we don't really use it).
        '''
        res = [[0, 0]]
        events = []

        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))

        events.sort()  # sort the events in left -> right order

        # We use heap for storing two key informations. 1. height of the building which we sort based on
        # 2. the ending of each starting point (we only store the starting points in heap)
        maxheap = [(0, float('inf'))]
        for l, negH, r in events:
            # 1. pos is the starting position of the current point.
            # if the building with the max height maxheap[0] already ended maxheap[0][1] <= pos we pop that
            # element. We continue poping elements from heap till this is not the case.
            while maxheap[0][1] <= l:
                heappop(maxheap)
            # 2. if it's the start-building event we push that to the heap.
            if negH:
                heappush(maxheap, (negH, r))

            # 3, Step 1 (removing elements from the heap) and 2 (add elements to the heap) can change the heap structure.
            # if the current event is a start event and  adding it in step 2 changes previous the maximum (res[-1][1] previous
            # maximum and -maxheap[0][0] is the current maximum we add it to the result. if it is the end event
            # and removing it from the heap in first step changes the maximum of the heap we add that to the results too.
            if res[-1][1] != -maxheap[0][0]:
                res.append([l, -maxheap[0][0]])

        return res[1:]


sol = Solution()
# buildings = [[0, 2, 3], [2, 5, 3]]
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(f'output: {sol.getSkyline(buildings)}')
