from heapq import heapify, heappop, heappush

class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        '''
        We will have a `mentions` list of size `numberOfUsers`
        We can use a heap for the events, sorted by TIMESTAMP and then "OFFLINE" first (we can store "OFFLINE" as 0 and "MESSAGE" as 1 or we just store as-is but sorted in descending)
            - If we see an "OFFLINE" event, we also create "ONLINE" event for the same user but at timestamp t+60
        We can also use a set to store the a list of online users, we use reference this list on whether the user receives the message event
        Each time we pop from the heap and there's OFFLINE event, we update the list of statuses to OFFLINE for the user
        '''
        event_type_map = {"ONLINE": 0, "OFFLINE": 1, "MESSAGE": 2}
        mentions = [0] * numberOfUsers
        heap = []
        ONLINE_TIME_OFFSET = 60
        online_users = set([i for i in range(numberOfUsers)])
        all_mentioned = 0
        # Add events into heap
        for type, time, users in events:
            heap.append((int(time), event_type_map[type], users))
            if type == 'OFFLINE':
                heap.append((int(time) + ONLINE_TIME_OFFSET, event_type_map["ONLINE"], users))

        heapify(heap)
        while heap:
            _, type, users = heappop(heap)
            if type == event_type_map["OFFLINE"]:
                online_users.discard(int(users))
                continue
            if type == event_type_map["ONLINE"]:
                online_users.add(int(users))
                continue
            if type == event_type_map["MESSAGE"]:
                if users == "HERE":
                    for user in online_users:
                        mentions[user] += 1
                    continue
                if users == "ALL":
                    all_mentioned += 1
                    continue
                user_list = users.split()
                for user in user_list:
                    user_id = int(user[2:])
                    mentions[user_id] += 1
                    
        
        for i in range(numberOfUsers):
            mentions[i] += all_mentioned

        return mentions
        
        
sol = Solution()
print(f'output: {sol.countMentions(numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]])}, expected: [2, 2]')
print(f'output: {sol.countMentions(numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]])}, expected: [2, 2]')
print(f'output: {sol.countMentions(numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]])}, expected: [0, 1]')