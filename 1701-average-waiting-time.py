from typing import List
from collections import deque

class Solution:
  def averageWaitingTime(self, customers: List[List[int]]) -> float:
    '''
    curTime variable
    waitingTimes array

    pop from queue, check the arrival time
      If arrival >= curTime, set curTime to arrival

    curTime += time[i]
    waitingTime = curTime - arrival
    
    add waitingTime to this array
    '''
    curTime = 0
    waitingTimes = []
    
    queue = deque(customers)
    while queue:
      arrival, time = queue.popleft()
      if arrival > curTime:
        curTime = arrival
      curTime += time
      waitingTime = curTime - arrival
      waitingTimes.append(waitingTime)

    return sum(waitingTimes) / len(waitingTimes)

sol = Solution()
# customers = [[1,2],[2,5],[4,3]]
customers = [[5,2],[5,4],[10,3],[20,1]]
print(f'output: {sol.averageWaitingTime(customers)}')