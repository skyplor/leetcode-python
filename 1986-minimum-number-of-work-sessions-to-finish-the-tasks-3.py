class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        '''
        We can use backtracking way which would be faster than the other 2 solutions
        We will track index of the task as well as a list of sessions that are currently open
        in the list of sessions, we will store the remainingSessionTime
        So whenever we have a new task, we decide if we want to include in the session based on whether we can fit the task. We will consider all possibilities of fitting the task into each possible session as well as creating a new session to house this new task
        '''

        tasks.sort(reverse=True)
        n = len(tasks)
        result = n
        
        def backtracking(i: int, sessions: list[int]):
            nonlocal result
            if len(sessions) >= result:
                return
            
            if i == n:
                result = min(result, len(sessions))
                return
            
            for j in range(len(sessions)):
                if sessions[j] >= tasks[i]:
                    sessions[j] -= tasks[i]
                    backtracking(i+1, sessions)
                    sessions[j] += tasks[i]
                    
            sessions.append(sessionTime - tasks[i])
            backtracking(i+1, sessions)
            sessions.pop()
            
        backtracking(0, [])
        return result


sol = Solution()
print(f'output: {sol.minSessions([1, 2, 3], 3)} expected: 2')
# print(f'output: {sol.minSessions([3, 1, 3, 1, 1], 8)} expected: 2')
# print(f'output: {sol.minSessions([1, 2, 3, 4, 5], 15)} expected: 1')
