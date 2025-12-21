class Solution:
    def largestGoodInteger(self, num: str) -> str:
        '''
        We go through each character in the string
        We have a `res` variable that stores the current maximum good integer
        We have a temp string that stores the current possible good integer.
            - At each iteration,
                - if the current character is == the first character of the temp string,
                    - append it, and check the length of this temp string
                    - if length of temp string == 3, check with the string stored in `res` and if larger, we replace it
                - else, replace this character with the temp

        return the `res`
        '''

        res = ''
        temp = ''
        for c in num:
            if temp and temp[0] == c:
                temp += c
                if len(temp) == 3:
                    res = max(res, temp)
            else:
                temp = c

        return res


sol = Solution()
print(f'output: {sol.largestGoodInteger("6777133339")}')
print(f'output: {sol.largestGoodInteger("2300019")}')
print(f'output: {sol.largestGoodInteger("42352338")}')
