from collections import defaultdict


class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        '''
        We need to note that negative numbers will not help increase the MEX.
        So if we have a negative number, possible operations:
            - add `value`
            - exclude the number
        If we have positive number, possible operations:
            - add `value`
            - subtract `value`
            - exclude the number

        Also, if the array is of length 5, the largest MEX we can go is 5 because the best case scenario is [0, 1, 2, 3, 4].

        A number can become any number in the form: `num + k*value`. and this formula has to be bounded by [0, n-1]
        We first count the number of occurrences of each remainder of (num % value)
        Next, we go through each value of from 0 to n-1, getting the remainder of it (i % value) and checking if we have any number that can fulfil this.
            If no, we have found the answer
            If yes, we decrement the count
        '''

        n = len(nums)
        count = defaultdict(int)

        for num in nums:
            count[num % value] += 1

        for i in range(n):
            mod = i % value
            if count[mod] == 0:
                return i
            count[mod] -= 1

        return n


sol = Solution()
print(
    f'output: {sol.findSmallestInteger([1, -10, 7, 13, 6, 8], 5)}, expected: 4')
print(
    f'output: {sol.findSmallestInteger([1, -10, 7, 13, 6, 8], 7)}, expected: 2')
print(
    f'output: {sol.findSmallestInteger([3, 0, 3, 2, 4, 2, 1, 1, 0, 4], 5)}, expected: 10')
print(
    f'output: {sol.findSmallestInteger([0, 3, -7, 1], 3)}, expected: 4')
