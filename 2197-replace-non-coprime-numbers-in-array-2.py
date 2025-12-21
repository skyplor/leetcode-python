import math


class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        '''
        We can create a stack to store our ans
        For each number in nums, we check if the num is coprime with the last number in our ans stack. If yes, we compute the lcm, update the value in ans. If no, we add this num into the ans stack and proceed to the next num
        '''
        ans = []
        for num in nums:
            while ans:
                if math.gcd(num, ans[-1]) > 1:
                    num = math.lcm(num, ans.pop())
                else:
                    break

            ans.append(num)

        return ans


sol = Solution()
nums = [6, 4, 3, 2, 7, 6, 2]
print(f'output: {sol.replaceNonCoprimes(nums)}, expected: [12, 7, 6]')
nums = [2, 2, 1, 1, 3, 3, 3]
print(f'output: {sol.replaceNonCoprimes(nums)}, expected: [2, 1, 1, 3]')
