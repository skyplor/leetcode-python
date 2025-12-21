class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''
        If we have 1 to 3 ones, then we at most can have 1 zero
        4 ones, at most is 2 zeros

        In reverse, if 1 zero, we will need 1 to 3 ones.

        Max number of zeros for s of length `n` = sqrt(n)
        We can build a list of zeros, then for each index i in s, we try to check the number of zeros

        Time complexity: O(n * sqrt(n))
        '''

        right = 0
        n = len(s)
        next_zero = [-1] * n

        prev = n
        for i in range(n-1, -1, -1):
            next_zero[i] = prev
            if s[i] == '0':
                prev = i

        res = 0

        for left in range(n):
            zeroes = 1 if s[left] == '0' else 0
            right = left

            while zeroes ** 2 <= n:
                next = next_zero[right]
                ones = next - left - zeroes
                if ones >= zeroes ** 2:
                    res += min(next - right, ones - (zeroes**2) + 1)
                zeroes += 1
                right = next
                if right == n:
                    break

        return res


sol = Solution()
print(f'output: {sol.numberOfSubstrings("00011")}, expected: 5')
print(f'output: {sol.numberOfSubstrings("101101")}, expected: 16')
