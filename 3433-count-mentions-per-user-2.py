from heapq import heapify, heappop, heappush

class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        '''
        We will have a `mentions` list of size `numberOfUsers`
        We sort the events based on timestamp and OFFLINE type first
        We also have a `users_online_time` where we set the time when the user is online
        Next we loop through events
            - if type is "OFFLINE", we update the `user_online_time` to the next time he will be online
            - if type is "MESSAGE",
                - if users is "HERE", we check through each user in `users_online_time` and if current time is greater than the online time, we add 1 to the mention count
                - if users is "ALL", we use a separate var to keep track and add this one shot later on for ALL users
                - if users is specific user, we can simply process the list of users and add to mentions
        '''
        # We sort by timestamp, then by type.
        # e[0] == 'MESSAGE' evaluates to False (0) if type is 'OFFLINE' and True (1) if type is 'MESSAGE',
        # and this helps to sort by 0 then 1
        events.sort(key=lambda e: (int(e[1]), e[0] == 'MESSAGE'))
        mentions = [0] * numberOfUsers
        ONLINE_TIME_OFFSET = 60
        users_online_time = [0] * numberOfUsers
        all_mentioned = 0
        
        for type, time, users in events:
            if type == "MESSAGE":
                if users == "HERE":
                    for user, online_time in enumerate(users_online_time):
                        if int(time) >= online_time:
                            mentions[user] += 1
                    continue
                if users == "ALL":
                    all_mentioned += 1
                    continue
                user_list = users.split()
                for user in user_list:
                    user_id = int(user[2:])
                    mentions[user_id] += 1
                continue
            users_online_time[int(users)] = int(time) + ONLINE_TIME_OFFSET
        
        for i in range(numberOfUsers):
            mentions[i] += all_mentioned

        return mentions
        
        
sol = Solution()
print(f'output: {sol.countMentions(numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]])}, expected: [2, 2]')
print(f'output: {sol.countMentions(numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]])}, expected: [2, 2]')
print(f'output: {sol.countMentions(numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]])}, expected: [0, 1]')