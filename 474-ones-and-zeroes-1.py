from functools import cache


class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        '''
        We can use DP for this.
        At each index, we either include it or don't include it.
        For our recursion, we need to calculate the number of 1s, 0s and cur_len
        Base case:
            - if number of ones and zeros == m and n, add 1 and return total length
        - if number of ones exceed n or number of zeros exceed m, don't include
        - else, can include or don't include

        Time (without cache): O(2^len(strs))
        Space (without cache): O(len(strs)) stack

        Time (with cache): O(len(strs) * m * n)
        '''

        @cache
        def recurse(i: int, zeros: int, ones: int) -> int:
            if i == len(strs):
                return 0

            cur_ones = strs[i].count('1')
            cur_zeros = len(strs[i]) - cur_ones

            cur_len = 0
            if zeros + cur_zeros <= m and ones + cur_ones <= n:
                cur_len = 1 + recurse(i+1, zeros + cur_zeros,
                                      ones + cur_ones)

            cur_len = max(cur_len, recurse(i+1, zeros, ones))

            return cur_len

        return recurse(0, 0, 0)


sol = Solution()
print(
    f'output: {sol.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3)}, expected: 4')
print(
    f'output: {sol.findMaxForm(strs=["10", "0", "1"], m=1, n=1)}, expected: 2')
