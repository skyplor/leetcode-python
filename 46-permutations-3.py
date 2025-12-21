from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Using iteration
        We start off with 1 empty list of list
        For each num, we have a new list (new_perms), then we have a loop that loop through each list of permutations
        With each loop, We will then insert the num into each position of the permutation
        Take note that the loop will loop to len(perms) + 1 as we are inserting an additional number
        Also take note that we need to make a copy of the perms before inserting so that we can reuse that perms for other loops
        After inserting, we then append into the new_perms list
        Then we assign this new_perms to the perms and go to the next num in the iteration
        E.g
            before inserting - perms: [[]], new_perms: []
            after inserting - perms: [[1]]

            before inserting - perms: [[1]], new_perms: []
            after inserting - perms: [[2, 1], [1, 2]]

            before inserting - perms: [[2, 1], [1, 2]], new_perms: []
            after inserting - perms: [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
        '''

        perms = [[]]

        for num in nums:
            new_perms = []

            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perms.append(p_copy)

            perms = new_perms

        return perms


sol = Solution()
nums = [1, 2, 3]
output = sol.permute(nums)
print(f'nums: {nums}\noutput: {output}')
