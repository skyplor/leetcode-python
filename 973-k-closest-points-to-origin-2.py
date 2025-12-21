from heapq import heappush, heappop


class Solution:
    def kClosest(self, points: list[list[int]], k: int):
        '''
        Closest means smallest distance from the point (0, 0)
        Using a heap for this, and keeping the size of the heap to be of size k.
        The heap will be a max heap so each time the size is larger than k,
            we pop the elements in the heap out and since it is a max heap,
            we ensure that the smaller items remain in the heap
        At the end, we pop out all the items in the heap and put into the result set
        Traverse through the points, calculate the distance for each point, add each point into heap as a tuple of distance and point (distance, [x, y])
        '''
        def distance_from_origin(x: int, y: int) -> int:
            return x**2 + y**2

        heap = []

        for x, y in points:
            distance = distance_from_origin(x, y)

            if len(heap) < k:
                heappush(heap, (-distance, [x, y]))
            elif distance < -heap[0][0]:
                heappop(heap)
                heappush(heap, (-distance, [x, y]))

        return [point for _, point in heap]


sol = Solution()
points = [[1, 3], [-2, 2]]
k = 1
output = sol.kClosest(points, k)
print(f'output: {output}')
