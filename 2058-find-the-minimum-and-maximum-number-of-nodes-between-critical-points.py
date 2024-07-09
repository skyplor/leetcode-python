from listnode import ListNode, toArray, generateListNodes
from typing import Optional, List

class Solution:
  def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
    '''
    3 points -> only 1 critical point
    4 points -> can potentially have 2 critical points e.g [1,4,3,5] -> local maxima: i = 1, local minima: i = 2

    if len(nodes) <= 3, return [-1, -1]
    we have 2 vars that stores the index of firstCritical and prevCritical points
    we also have 1 var that stores the minDistance

    Loop through the linked list and populate the vars:
      - each time we have a critical point
        - if first Critical is -1, store current index as first Critical
        - check prev Critical point and update minDistance if this is smaller
        - populate the prev critical point to this critical point
    Lastly, we return the results in an array
    '''

    minDistance = float("inf")
    firstCritical = -1
    prevCritical = -1
    cur, prevNode = head, None
    idx = 0
    while cur:
      idx += 1
      nextNode = cur.next
      if prevNode and nextNode:
        isCriticalPoint = (prevNode.val > cur.val and nextNode.val > cur.val) or (prevNode.val < cur.val and nextNode.val < cur.val)
        if isCriticalPoint:
          if firstCritical == -1:
            firstCritical = idx
          if prevCritical != -1:
            currentDistance = idx - prevCritical
            minDistance = min(minDistance, currentDistance)
          prevCritical = idx
      prevNode = cur
      cur = nextNode
      
    if firstCritical == -1 or firstCritical == prevCritical:
      return [-1, -1]

    maxDistance = prevCritical - firstCritical
    return [minDistance, maxDistance]
  
sol = Solution()
# head = generateListNodes([3,1])
# head = generateListNodes([5,3,1,2,5,1,2])
head = generateListNodes([1,3,2,2,3,2,2,2,7])
print(f'output: {sol.nodesBetweenCriticalPoints(head)}')