from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
      # need 2 heaps and we just get the top 2 from the heaps.
      # difference between those 2 heaps are that first heap will have elements that are all smaller than 2nd heap
      # length of each heap will be ~ similar. Difference will be at most by 1
      # if one heap has 2 or more elements than another heap, we will need to pop from that heap and push into the other heap
      # the heap that has all smaller elements will be implemented as maxheap while the other will be minheap
      # because we want to be able to move the largest from the left heap to the right heap,
      # and to move the smallest from the right heap to left heap
      self.leftMaxHeap = []
      self.rightMinHeap = []

    def addNum(self, num: int) -> None:
      # all elements on the left heap must be less than right heap
      # so we need to get the top item in the 2 heaps, compare the num of both and decide where to put it
      if self.rightMinHeap and num > self.rightMinHeap[0]:
        heappush(self.rightMinHeap, num)
      else:
        heappush(self.leftMaxHeap, -num)

      if len(self.leftMaxHeap) - len(self.rightMinHeap) > 1:
        # shift the items
        largestItemFromLeft = -heappop(self.leftMaxHeap)
        heappush(self.rightMinHeap, largestItemFromLeft)
      elif len(self.rightMinHeap) - len(self.leftMaxHeap) > 1:
        # shift the items
        smallestItemFromRight = heappop(self.rightMinHeap)
        heappush(self.leftMaxHeap, -smallestItemFromRight)

    def findMedian(self) -> float:
      if len(self.leftMaxHeap) > len(self.rightMinHeap):
        return -self.leftMaxHeap[0]
      elif len(self.rightMinHeap) > len(self.leftMaxHeap):
        return self.rightMinHeap[0]
      # even, we get from both
      left_item, right_item = -self.leftMaxHeap[0], self.rightMinHeap[0]
      return (left_item + right_item) / 2
    
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())