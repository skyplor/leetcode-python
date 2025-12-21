from collections import defaultdict
from heapq import heapify, heappop, heappush


class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        '''
        Strategy: Use a min-heap to track which full lakes will rain next (sorted by urgency).

        Key insight: When we have a dry day, we should prioritize drying the lake that will 
        flood soonest, not the one that rains most frequently.

        Data structures:
        - next_lake_idx: Maps each lake to a list of ALL indices where it rains
        - lake_idx_pointer: Tracks current position in next_lake_idx for each lake (avoids O(n) pop(0))
        - lake_state: Tracks whether each lake is currently full (True) or empty (False)
        - min_heap: Contains (next_rain_index, lake) for all currently full lakes that will rain again
        - ans: Result array (-1 for rain days, lake number for dry days)

        Algorithm:
        1. Preprocess: Build next_lake_idx mapping for all lakes

        2. Iterate through each day:
        
        If it rains (lake > 0):
        - Check if lake is already full → if yes, flood occurs, return []
        - Mark lake as full, set ans[i] = -1
        - Increment lake_idx_pointer[lake] to move to next occurrence
        - If lake has more future occurrences:
            * Get next rain index using pointer (O(1) access, no expensive pop!)
            * Add (next_rain_index, lake) to min_heap
        
        If it's a dry day (lake == 0):
        - Default: ans[i] = 1 (dry any lake)
        - If min_heap is not empty:
            * Pop the lake with earliest next rain (most urgent)
            * Dry it: set lake_state to False
            * Update ans[i] to the dried lake number

        Key optimization: Using lake_idx_pointer instead of pop(0) reduces time complexity
        from O(n²) to O(n log n).

        Time: O(n log n) - heap operations dominate, no O(n) list operations
        Space: O(n) - for heap and tracking structures
        '''
        min_heap = []
        next_lake_idx = defaultdict(list)
        lake_idx_pointer = defaultdict(int)
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

                    lake_idx_pointer[lake] += 1
                    if lake_idx_pointer[lake] < len(next_lake_idx[lake]):
                        heappush(min_heap, (next_lake_idx[lake][lake_idx_pointer[lake]], lake))
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
