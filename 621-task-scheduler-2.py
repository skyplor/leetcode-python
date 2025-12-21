from collections import defaultdict, deque
from heapq import heapify, heappop, heappush


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        '''
        For a start, we will need to use greedy approach to process the most frequent task first. So we need to count the number of occurrences of each task
        We then add the counts to a max heap so each time we pop, we get the one with the most count in O(log n)
        The heap will be the place where we store tasks that are available for processing. So if a task is just processed, we can't add it back immediately into the heap. Instead, we need to wait n amount of time before it gets added back
        We will have a queue to store those tasks that we have just processed but cannot add into heap yet
            - the queue will store the count and the next interval available for processing e.g (-2, 2)
        At each loop, we will check and if heap or queue isn't empty, that means we still have tasks to process.
            - If heap is already empty, but queue isn't, that means we don't have any task to process at this point, and we need to fast-forward the interval to the next task available in the queue
                - So we increment the interval to the interval of the next item in the queue
            - If heap isn't empty, we process from the heap. Next, check the queue to see if the interval has reached. If yes, add into heap to be processed at the next interval
        We will have an `interval` variable that stores how long it has past and return it
        '''
        interval = 0
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        max_heap = [-count for count in counts.values()]
        heapify(max_heap)

        queue = deque()
        while queue or max_heap:
            interval += 1

            # Process a task if available
            if max_heap:
                next_task_count = heappop(max_heap)
                next_task_count += 1
                if next_task_count < 0:
                    queue.append([next_task_count, interval + n])

            # Check if any tasks in queue are ready to be processed
            if queue and queue[0][1] == interval:
                next_count, _ = queue.popleft()
                heappush(max_heap, next_count)

        return interval


sol = Solution()
# tasks = ["A","A","A","B","B","B"]
# n = 2
# tasks = ["A","C","A","B","D","B"]
# n = 1
# tasks = ["A", "A", "A", "B", "B", "B"]
# n = 3
tasks = ["A", "A", "A", "B", "B", "B", "C",
         "D", "E", "F", "G", "H", "I", "J", "K"]
n = 7
output = sol.leastInterval(tasks, n)
print(f'tasks: {tasks}\nn: {n}\noutput: {output}')
