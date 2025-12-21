from collections import defaultdict
from heapq import heapify, heappop, heappush


class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        '''
        Strategy: Use a min-heap to track which full lakes will rain next (sorted by urgency).

        Key insight: When we have a dry day, we should prioritize drying the lake that will 
        flood soonest, not the one that rains most frequently.

        Data structures:
        - next_lake_idx: Maps each lake to a list of all indices where it rains
        - lake_state: Tracks whether each lake is currently full (True) or empty (False)
        - min_heap: Contains (next_rain_index, lake) for all currently full lakes that will rain again
        - ans: Result array (-1 for rain days, lake number for dry days)

        Algorithm:
        1. Preprocess: Build next_lake_idx mapping for all lakes

        2. Iterate through each day:

        If it rains (lake > 0):
        - Check if lake is already full → if yes, flood occurs, return []
        - Mark lake as full, set ans[i] = -1
        - Remove current occurrence from next_lake_idx
        - If lake will rain again in future, add (next_rain_index, lake) to min_heap

        If it's a dry day (lake == 0):
        - Default: ans[i] = 1 (dry any lake)
        - If min_heap is not empty:
            * Pop the lake with earliest next rain (most urgent)
            * Dry it: set lake_state to False
            * Update ans[i] to the dried lake number
            * Note: We don't re-add to heap since it's now empty

        Time: O(n log n) - heap operations
        Space: O(n) - for heap and tracking structures
        '''
        min_heap = []
        next_lake_idx = defaultdict(list)
        for i, lake in enumerate(rains):
            next_lake_idx[lake].append(i)

        lake_state = defaultdict(bool)
        ans = [0] * len(rains)
        for i, lake in enumerate(rains):
            if lake > 0:
                if lake_state[lake]:
                    return []
                else:
                    lake_state[lake] = True
                    ans[i] = -1
                    if next_lake_idx[lake]:
                        next_lake_idx[lake].pop(0)
                    if next_lake_idx[lake]:
                        heappush(min_heap, (next_lake_idx[lake][0], lake))
            else:
                ans[i] = 1
                if min_heap:
                    _, next_lake = heappop(min_heap)
                    lake_state[next_lake] = False
                    ans[i] = next_lake

        return ans


sol = Solution()
print(f'output: {sol.avoidFlood([1, 2, 3, 4])}, expected: [-1,-1,-1,-1]')
print(
    f'output: {sol.avoidFlood([1, 2, 0, 0, 2, 1])}, expected: [-1,-1,2,1,-1,-1]')
print(f'output: {sol.avoidFlood([1, 2, 0, 1, 2])}, expected: []')
print(
    f'output: {sol.avoidFlood([1, 2, 0, 2, 3, 0, 1])}, expected: [-1, -1, 2, -1, -1, 1, -1]')
