class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        '''
        Maintain a checklist of adjacent row pairs that are still tied (equal in kept columns).

        For each column:
        - If any tied pair violates order: delete column, recheck same pairs next time
        - If column is valid: remove settled pairs from checklist, keep only tied pairs
        - If checklist becomes empty: all pairs are sorted, done!
        '''

        to_del = 0
        checklist = range(len(strs) - 1)

        for j in range(len(strs[0])):

            new_checklist = []
            should_delete = False

            for i in checklist:
                if strs[i][j] > strs[i+1][j]:
                    to_del += 1
                    should_delete = True
                    break

                elif strs[i][j] == strs[i+1][j]:
                    new_checklist.append(i)

            if not should_delete:
                if not new_checklist:
                    return to_del
                checklist = new_checklist

        return to_del


sol = Solution()
print(f'output: {sol.minDeletionSize(["ca", "bb", "ac"])}, expected: 1')
print(f'output: {sol.minDeletionSize(["xc", "yb", "za"])}, expected: 0')
print(f'output: {sol.minDeletionSize(["zyx", "wvu", "tsr"])}, expected: 3')
