class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        '''
        For each task, either we include in current session, or we don't include. If we don't include, we just increase the index.
        We also need a way to keep track of completed tasks. We can add the index into a set for completed tasks
        base case would be when our index reach end of tasks list

        while there are still tasks not completed, i.e. len(set) < len(tasks), we loop through each tasks again
        
        But this approach is very inefficient and will encounter max recursion depth error
        '''

        def f(i: int, completed_tasks: set, remaining_session_time: int, number_of_sessions: int) -> int:
            print(f'i: {i}, completed_tasks: {completed_tasks}, remaining_session_time: {remaining_session_time}, number_of_sessions: {number_of_sessions}')
            if (i > len(tasks) - 1 and len(completed_tasks) == len(tasks)) or remaining_session_time == 0:
                return number_of_sessions

            if i > len(tasks) - 1:
                return f(0, completed_tasks, sessionTime, number_of_sessions + 1)

            number_of_sessions_if_include = number_of_sessions_if_exclude = number_of_sessions
            if tasks[i] <= remaining_session_time and i not in completed_tasks:
                # can either include or not include
                completed_tasks.add(i)
                number_of_sessions_if_include = f(
                    i+1, completed_tasks, remaining_session_time - tasks[i], number_of_sessions)
                completed_tasks.remove(i)

            number_of_sessions_if_exclude = f(
                i+1, completed_tasks, remaining_session_time, number_of_sessions)

            return min(number_of_sessions_if_include, number_of_sessions_if_exclude)

        return f(0, set(), sessionTime, 1)


sol = Solution()
print(f'output: {sol.minSessions([1, 2, 3], 3)} expected: 2')
# print(f'output: {sol.minSessions([3, 1, 3, 1, 1], 8)} expected: 2')
# print(f'output: {sol.minSessions([1, 2, 3, 4, 5], 15)} expected: 1')
