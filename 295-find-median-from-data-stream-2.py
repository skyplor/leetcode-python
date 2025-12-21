from heapq import heappush, heappop


class MedianFinder:
    '''
    We can make use of 2 heaps, 1 max-heap and 1 min-heap
    max heap will contain all numbers smaller than numbers in min heap
    [max-heap, min-heap]
    each time we add a number, we add to max-heap first
    Then we need to ensure both conditions passes:
        1. ALL numbers in max-heap must be less than or equal to ALL numbers in min-heap
            - Get the largest number in the max-heap and compare with smallest number in min-heap. If it is larger than smallest number in min-heap, move it into min-heap
        2. Size of both heaps cannot differ by more than 1
            - Check size of both heaps and if 1 of them is greater by > 1, then we pop from that and push into the other

    For findMedian, we check if the size of both heaps are the same. If same, get the first element from both and divide by 2. If different, then we get from the larger heap
    '''

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -1 * num)
        # check if ALL numbers less than or equal to min-heap
        if len(self.maxHeap) > 0 and len(self.minHeap) > 0 and (self.maxHeap[0] * -1) > self.minHeap[0]:
            heappush(self.minHeap, heappop(self.maxHeap) * -1)

        while len(self.maxHeap) - len(self.minHeap) > 1:
            heappush(self.minHeap, heappop(self.maxHeap) * -1)
        while len(self.minHeap) - len(self.maxHeap) > 1:
            heappush(self.maxHeap, heappop(self.minHeap) * -1)

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return ((self.maxHeap[0] * -1) + self.minHeap[0]) / 2

        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]

        return self.maxHeap[0] * -1


medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())
