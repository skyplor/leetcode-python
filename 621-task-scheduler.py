from collections import Counter, deque
from typing import List
from heapq import heapify, heappop, heappush

class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    if not tasks: return 0

    interval = 0
    count = Counter(tasks)
    maxheap = [-cnt for cnt in count.values()]
    
    heapify(maxheap)
    
    interval = 0
    q = deque()

    while q or maxheap:
      interval += 1

      if not maxheap:
        interval = q[0][1]
      else:
        processed_item = heappop(maxheap)
        item_count = -processed_item - 1
        if item_count > 0:
          q.append([-item_count, interval + n])

      if q and q[0][1] == interval:
        next_item = q.popleft()
        heappush(maxheap, next_item[0])

    return interval
      
sol = Solution()
# tasks = ["A","A","A","B","B","B"]
# n = 2
# tasks = ["A","C","A","B","D","B"]
# n = 1
tasks = ["A","A","A", "B","B","B"]
n = 3
output = sol.leastInterval(tasks, n)
print(f'tasks: {tasks}\nn: {n}\noutput: {output}')