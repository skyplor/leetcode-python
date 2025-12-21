class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        '''
        
        '''
        n, m = len(skill), len(mana)
        end_times = [0] * n

        # initialise end_times for potion 1
        for i in range(n):
            if i > 0:
                end_times[i] += end_times[i-1]
            end_times[i] += skill[i] * mana[0]

        for j in range(1, m):
            for k in range(n):
                max_end = end_times[k] if k == 0 or end_times[k] > end_times[k - 1] else end_times[k - 1]
                end_times[k] = max_end + (skill[k] * mana[j])
            for l in range(n-2, -1, -1):
                end_times[l] = end_times[l+1] - (skill[l+1] * mana[j])

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
