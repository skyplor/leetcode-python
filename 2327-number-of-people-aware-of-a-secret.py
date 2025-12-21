from collections import deque


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        '''
        E.g
            - n = 4, delay = 1, forget = 3
            n = 1
                - [[1, 3]]
            n = 2
                - [[0, 2], [1, 3]]
            n = 3
                - [[0, 1], [0, 2], [1, 3], [1, 3]]
            n = 4
                - [[0, 1], [0, 2], [0, 2], [1, 3], [1, 3], [1, 3]]

        We can store 2 counters for each person, starting on the day of discovery, one counter for delay, another for forget.
        Each day, we retrieve all the people, decrements the delay and forget.
            - if forget == 0, we remove this person
            - if delay == 0, this person can share, so we create another person and add both to total count, and push both the people back in
            - else, push the person back
            - if current_day == n: return total count
            
        Instead of this, we can store how many people that are newly created
        E.g
            - n = 4, delay = 1, forget = 3
            n = 1
                - [[1, 1, 3]]
            n = 2
                - [[1, 0, 2], [1, 1, 3]]
            n = 3
                - [[1, 0, 1], [1, 0, 2], [2, 1, 3]]
            n = 4
                - [[1, 0, 1], [2, 0, 2], [3, 1, 3]]
        '''
        queue = deque([[1, delay, forget]])
        total_count = 0
        for _ in range(1, n):

            for _ in range(len(queue)):
                count, cur_delay, cur_forget = queue.popleft()
                if cur_delay > 0:
                    cur_delay -= 1
                    if cur_delay == 0:
                        total_count += count
                cur_forget -= 1
                if cur_forget == 0:
                    total_count -= count
                    continue

                queue.append([count, cur_delay, cur_forget])

            queue.append([total_count, delay, forget])
            
        total_count = 0
        while queue:
            count, _, _ = queue.popleft()
            total_count += count

        return total_count % ((10 ** 9) + 7)


sol = Solution()
n = 6
delay = 2
forget = 4
print(f'output: {sol.peopleAwareOfSecret(n, delay, forget)}, expected; 5')
n = 4
delay = 1
forget = 3
print(f'output: {sol.peopleAwareOfSecret(n, delay, forget)}, expected; 6')
