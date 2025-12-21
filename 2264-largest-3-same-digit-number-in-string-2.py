class Solution:
    def largestGoodInteger(self, num: str) -> str:
        '''
        We have a `res` variable that stores the current maximum good integer
        We go through each character in the string
            - At each iteration,
                - if the current character == next character == next next character
                    - compare and replace with res

        return `res`
        '''

        res = ''
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, num[i:i+3])

        return res


sol = Solution()
print(f'output: {sol.largestGoodInteger("6777133339")}')
print(f'output: {sol.largestGoodInteger("2300019")}')
print(f'output: {sol.largestGoodInteger("42352338")}')
