from collections import defaultdict


class Solution:
    def numSub(self, s: str) -> int:
        '''
        We find the gaps (or groups of ones), count how many are there, differentiated by the length of the substring.
        Next, we calculate how many subgroups are there for each group using math formula (e.g 2 ones = 3, 3 ones = 6, 4 ones = 10, 5 ones = 15)
        Formula is (n (n + 1)) / 2
        '''
        one_groupings = defaultdict(int)
        ones_count = 0
        for c in s:
            if c == '0':
                one_groupings[ones_count] += 1
                ones_count = 0
                continue

            ones_count += 1
        one_groupings[ones_count] += 1

        res = 0
        for subgroup, count in one_groupings.items():
            res += count * (((subgroup) * (subgroup + 1)) // 2)
            res %= (10**9) + 7

        return res


sol = Solution()
print(f'output: {sol.numSub("0110111")}, expected: 9')
print(f'output: {sol.numSub("101")}, expected: 2')
print(f'output: {sol.numSub("111111")}, expected: 21')
