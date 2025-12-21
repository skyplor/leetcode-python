import java.util.*;

class LcMinimumNumberWorkSessionsSolution {
    /*
     * We can use backtracking way which would be faster than the other 2 solutions
     * We will track index of the task as well as a list of sessions that are
     * currently open
     * in the list of sessions, we will store the remainingSessionTime
     * So whenever we have a new task, we decide if we want to include in the
     * session based on whether we can fit the task. We will consider all
     * possibilities of fitting the task into each possible session as well as
     * creating a new session to house this new task
     */

    public static int result;

    public int minSessions(int[] tasks, int sessionTime) {
        Arrays.sort(tasks);
        for (int i = 0, j = tasks.length - 1; i < j; i++, j--) {
            int temp = tasks[i];
            tasks[i] = tasks[j];
            tasks[j] = temp;
        }
        int n = tasks.length;
        result = n;

        backtracking(tasks, sessionTime, 0, new ArrayList<Integer>());

        return result;
    }

    public void backtracking(int[] tasks, int sessionTime, int index, List<Integer> sessions) {
        if (sessions.size() >= result) {
            return;
        }

        if (index == tasks.length) {
            result = Math.min(result, sessions.size());
            return;
        }

        for (int i = 0; i < sessions.size(); i++) {
            int session = sessions.get(i);
            if (session >= tasks[index]) {

                sessions.set(i, session - tasks[index]);
                backtracking(tasks, sessionTime, index + 1, sessions);
                sessions.set(i, session);
            }
        }
        sessions.add(sessionTime - tasks[index]);
        backtracking(tasks, sessionTime, index + 1, sessions);
        sessions.remove(sessions.size() - 1);
    }

    public static void main(String[] args) {
        LcMinimumNumberWorkSessionsSolution sol = new LcMinimumNumberWorkSessionsSolution();

        System.out.println("output: " + sol.minSessions(new int[] { 1, 2, 3 }, 3) + ", expected: 2");
    }

}
