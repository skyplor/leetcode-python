class Solution:
    def maxOperations(self, s: str) -> int:
        '''
        We have an index that is the length of the string `s`. While this index is not == 0,
        we can check the LSB character. If LSB is a zero, we want to add 1 as the gap before hitting a 1.
        we store this value `total_gaps`.
        In the process, we move the pointer `i` to point to the next char of s
        Once we find a `1`, the number of operations to remove this `1` will be based on the value `total_gaps` we have stored
        total_ops += total_gaps
        during each iteration, we reduce the index
        '''
        n = len(s)
        i = n - 1
        total_ops = 0
        total_gaps = 0
        while i >= 0:
            if s[i] == '1':
                total_ops += total_gaps
                i -= 1
            else:
                total_gaps += 1
                while i >= 0 and s[i] == '0':
                    i -= 1
            
        return total_ops


sol = Solution()
print(f'output: {sol.maxOperations("1001101")}, expected: 4')
print(f'output: {sol.maxOperations("00111")}, expected: 0')
