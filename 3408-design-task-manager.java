import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.HashMap;
import java.util.Arrays;

class TaskManager {
    /**
     * We can have a max_heap that will prioritise based on priority, then taskId,
     * followed by userId.
     * As the default is a min_heap, we will multiply `-1` to each priority to make
     * it max_heap
     *
     * constructor:
     * - we will have a hashmap that contains the taskId and the priority. Key:
     * taskId, Value: (priority, userId)
     * - This allows us to do lazy deletion later on so it is faster during `edit`
     * and `rmv`.
     * - During execTop, we will then get the top task and check against this
     * hashmap.
     * - If task exist, match the priority.
     * - If both matches, execute that.
     * - Else remove it
     * - we first initialise a max_heap
     * - for each task, we add into the max_heap as a tuple in the form
     * (-priority_1, -taskId_1, userId_1)
     * - at the end, we use heapify*
     *
     * add:
     * - similar to how __init__ does it, but we use heappush to push the tuple into
     * the existing max_heap
     * - We also need to add this new entry into the hashmap*
     *
     * edit:
     * - this will be similar to `add`, except that we will update the hashmap with
     * the new priority*
     *
     * rmv:
     * - we will only remove the taskId from hashmap*
     *
     * execTop:
     * - We will retrieve the top task from max_heap
     * - Next, we check with the hashmap
     * - If task exist, match the priority.
     * - If both matches, execute that.
     * - Else remove it
     * 
     */

    Map<Integer, int[]> taskPriority = new HashMap<>();
    Queue<int[]> maxPriorityQueue = new PriorityQueue<>((a, b) -> {
        int cmp = Integer.compare(b[0], a[0]);
        return cmp != 0 ? cmp : Integer.compare(b[1], a[1]);
    });

    public TaskManager(List<List<Integer>> tasks) {
        for (List<Integer> task : tasks) {
            int userId = task.get(0);
            int taskId = task.get(1);
            int priority = task.get(2);
            this.taskPriority.put(taskId, new int[] { priority, userId });
            this.maxPriorityQueue.offer(new int[] { priority, taskId, userId });
        }
    }

    public void add(int userId, int taskId, int priority) {
        this.taskPriority.put(taskId, new int[] { priority, userId });
        this.maxPriorityQueue.offer(new int[] { priority, taskId, userId });
    }

    public void edit(int taskId, int newPriority) {
        int[] priorityAndUserId = this.taskPriority.get(taskId);
        int userId = priorityAndUserId[1];
        this.taskPriority.put(taskId, new int[] { newPriority, userId });
        this.maxPriorityQueue.offer(new int[] { newPriority, taskId, userId });
    }

    public void rmv(int taskId) {
        this.taskPriority.remove(taskId);
    }

    public int execTop() {
        while (this.maxPriorityQueue.size() > 0) {
            int[] task = this.maxPriorityQueue.poll();
            int priority = task[0];
            int taskId = task[1];
            int userId = task[2];
            if (!this.taskPriority.containsKey(taskId)) {
                continue;
            }

            int[] priorityAndUserId = this.taskPriority.get(taskId);

            if (priority != priorityAndUserId[0] || userId != priorityAndUserId[1]) {
                continue;
            }

            this.taskPriority.remove(taskId);
            return userId;
        }

        return -1;

    }

    public static void main(String[] args) {
        TaskManager taskManager = new TaskManager(
                Arrays.asList(Arrays.asList(1, 101, 10), Arrays.asList(2, 102, 20), Arrays.asList(3, 103, 15)));
        taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4.
        taskManager.edit(102, 8); // Updates priority of task 102 to 8.
        System.out.println(String.format("output: %d, expected: 3", taskManager.execTop())); // return 3. Executes task
                                                                                             // 103 for User 3.
        taskManager.rmv(101); // Removes task 101 from the system.
        taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5.
        System.out.println(String.format("output: %d, expected: 5", taskManager.execTop())); // return 5. Executes task
                                                                                             // 105 for User 5.
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager obj = new TaskManager(tasks);
 * obj.add(userId,taskId,priority);
 * obj.edit(taskId,newPriority);
 * obj.rmv(taskId);
 * int param_4 = obj.execTop();
 */