class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        '''
        If we calculate this manually, and we do precompute

        We will only need to determine the start time of the first wizard to ensure that that particular potion is brewed properly
        We need to calculate the end time of each wizard for the previous brew process. We will need to ensure that the LAST wizard can only start AFTER finishing the previous potion,
            - hence we will do the calculation in reverse, starting from the last wizard.
            - However, there's another problem here. If we only take the last timing from LAST wizard, it might overlap for some wizards in the middle. When that happens, we will need to push back the start time
            - see e.g for potion 3, if we use 64 as start time of wizard 4, wizard 3 will need to start at 56. But wizard 3 will only be done with potion 2 at time 60.
                - Also, Wizard 2 will also need to start much earlier before he finished with potion 2.
            - So we will use the end time of last wizard as the base and work backwards.
            - If we encounter a start time for current potion that is before the end time of previous potion, we update the start and end time of all wizards we have calculated

            e.g. skill = [1,5,2,4], mana = [5,1,4,2]
            - Potion 1:
                - Time taken: 5, 25, 10, 20
                - Start & end time: [0, 5], [5, 30], [30, 40], [40, 60] 
            - Potion 2:
                - Time taken: 1, 5, 2, 4
                - Start & end time: [52, 53], [53, 58], [58, 60], [60, 64]
            - Potion 3:
                - Time taken: 4, 20, 8, 16
                - Start & end time: [54, 58], [58, 78], [78, 86], [86, 102]
            - Potion 4:
                - Time taken: 2, 10, 4, 8
                - Start & end time: [86, 88], [88, 98], [98, 102], [102, 110]

        We don't really need to store the start time since it is the same as the end time of previous wizard. So we will only need a list of end times.

        We can have 2-pass inside the mana loop instead of having the recalculation loop in first solution
        '''
        n, m = len(skill), len(mana)
        end_times = [0] * n

        # initialise end_times for potion 1
        for i in range(n):
            if i > 0:
                end_times[i] += end_times[i-1]
            end_times[i] += skill[i] * mana[0]

        for j in range(1, m):
            end_times[n-1] += skill[n-1] * mana[j]
            for k in range(n-2, -1, -1):

                temp_end_time = end_times[k+1] - (skill[k+1] * mana[j])
                start_time = temp_end_time - (skill[k] * mana[j])
                if start_time > end_times[k]:
                    end_times[k] = temp_end_time
                else:
                    end_times[k] += skill[k] * mana[j]

            for l in range(1, n):
                end_times[l] = end_times[l-1] + (skill[l] * mana[j])

        return end_times[n-1]


sol = Solution()
skill = [1, 5, 2, 4]
mana = [5, 1, 4, 2]
print(f'output: {sol.minTime(skill, mana)}, expected: 110')
skill = [1, 1, 1]
mana = [1, 1, 1]
print(f'output: {sol.minTime(skill, mana)}, expected: 5')
skill = [1, 2, 3, 4]
mana = [1, 2]
print(f'output: {sol.minTime(skill, mana)}, expected: 21')
