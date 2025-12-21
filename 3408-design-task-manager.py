from typing import List
from heapq import heapify, heappush, heappop


class TaskManager:
    '''
    We can have a max_heap that will prioritise based on priority, then taskId, followed by userId.
    As the default is a min_heap, we will multiply `-1` to each priority to make it max_heap

    __init__:
        - we will have a hashmap that contains the taskId and the priority. Key: taskId, Value: (priority, userId)
            - This allows us to do lazy deletion later on so it is faster during `edit` and `rmv`.
            - During execTop, we will then get the top task and check against this hashmap.
            - If task exist, match the priority.
                - If both matches, execute that.
                - Else remove it
        - we first initialise a max_heap
        - for each task, we add into the max_heap as a tuple in the form (-priority_1, -taskId_1, userId_1)
        - at the end, we use heapify

    add:
        - similar to how __init__ does it, but we use heappush to push the tuple into the existing max_heap
        - We also need to add this new entry into the hashmap

    edit:
        - this will be similar to `add`, except that we will update the hashmap with the new priority

    rmv:
        - we will only remove the taskId from hashmap

    execTop:
        - We will retrieve the top task from max_heap
        - Next, we check with the hashmap
        - If task exist, match the priority.
            - If both matches, execute that.
            - Else remove it
    '''

    def __init__(self, tasks: List[List[int]]):
        self.task_priority = {}
        self.max_heap = []
        for user_id, task_id, priority in tasks:
            self.task_priority[task_id] = (priority, user_id)
            self.max_heap.append((-priority, -task_id, user_id))

        heapify(self.max_heap)

    def add(self, user_id: int, task_id: int, priority: int) -> None:
        self.task_priority[task_id] = (priority, user_id)
        heappush(self.max_heap, (-priority, -task_id, user_id))

    def edit(self, task_id: int, new_priority: int) -> None:
        _, user_id = self.task_priority[task_id]
        self.task_priority[task_id] = (new_priority, user_id)
        heappush(self.max_heap, (-new_priority, -task_id, user_id))

    def rmv(self, task_id: int) -> None:
        del self.task_priority[task_id]

    def execTop(self) -> int:
        while self.max_heap and ((-self.max_heap[0][1] not in self.task_priority) or (-self.max_heap[0][0] != self.task_priority[-self.max_heap[0][1]][0]) or self.max_heap[0][2] != self.task_priority[-self.max_heap[0][1]][1]):
            heappop(self.max_heap)

        if self.max_heap:
            _, task_id, user_id = heappop(self.max_heap)
            self.rmv(-task_id)
            return user_id

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

# taskManager = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
# taskManager.add(4, 104, 5)  # Adds task 104 with priority 5 for User 4.
# taskManager.edit(102, 8)  # Updates priority of task 102 to 8.
# print(f'output: {taskManager.execTop()}, expected: 3')  # return 3. Executes task 103 for User 3.
# taskManager.rmv(101)  # Removes task 101 from the system.
# taskManager.add(5, 105, 15)  # Adds task 105 with priority 15 for User 5.
# print(f'output: {taskManager.execTop()}, expected: 5')  # return 5. Executes task 105 for User 5.


taskManager = TaskManager([[1, 101, 8], [2, 102, 20], [3, 103, 5]])
taskManager.add(4, 104, 5)
taskManager.edit(102, 9)
print(f'output: {taskManager.execTop()}, expected: 2')
taskManager.rmv(101)
taskManager.add(50, 101, 8)
print(f'output: {taskManager.execTop()}, expected: 50')
