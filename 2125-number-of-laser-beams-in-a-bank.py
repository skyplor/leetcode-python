class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        '''
        If there exist a row that is empty, all '0's, then we can just exclude that row
        We go through each row starting from row 1 (0-indexed) and calculate how many security devices are there in the current and previous row. Then we multiply both numbers to get the total number of lasers between these 2 rows.
        Next, we set the current row's security devices as the prev and continue all the way to the last row
        '''
        res = prev = 0
        for i in range(len(bank)):
            cur = bank[i].count('1')
            if cur == 0:
                continue
            res += prev * cur
            prev = cur
            
        return res


sol = Solution()
print(
    f'output: {sol.numberOfBeams(["011001", "000000", "010100", "001000"])}, expected: 8')
print(f'output: {sol.numberOfBeams(["000", "111", "000"])}, expected: 0')
