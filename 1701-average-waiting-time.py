from typing import List

class Solution:
  def averageWaitingTime(self, customers: List[List[int]]) -> float:
    '''
    curTime variable
    waitingTime variable

    pop from queue, check the arrival time
      If arrival >= curTime, set curTime to arrival

    curTime += time[i]
    waitingTime += curTime - arrival
    '''
    curTime = 0
    waitingTime = 0
    for arrival, time in customers:
      if arrival > curTime:
        curTime = arrival
      curTime += time
      waitingTime += curTime - arrival

    return waitingTime / len(customers)

sol = Solution()
# customers = [[1,2],[2,5],[4,3]]
customers = [[5,2],[5,4],[10,3],[20,1]]
print(f'output: {sol.averageWaitingTime(customers)}')