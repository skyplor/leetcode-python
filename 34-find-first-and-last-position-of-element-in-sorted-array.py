class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        '''
        Using binary search, instead of returning directly when we find the target, we need to be able to find the start and end indices.
        We can do the binary search 2 times. once for the start position, another time for end position
        We also need a res variable to store the possible index found
        For start position,
            binary search, if found the target, continue to go to the left

        For end position,
            binary search, if found the target, continue to go to the right

        at the end, we return res
        '''

        def binary_search(find_start: bool):
            left, right = 0, len(nums)
            res = -1
            while left < right:
                mid = left + (right - left) // 2
                if target == nums[mid]:
                    res = mid
                    if find_start:
                        # go to left if found for find_start == True, else go to right
                        right = mid
                    else:
                        left = mid + 1
                elif target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1

            return res

        res = [-1, -1]

        res[0] = binary_search(True)
        if res[0] > -1:
            res[1] = binary_search(False)
        return res


sol = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
# target = 11
# target = 6
# nums = [1]
# target = 1
output = sol.searchRange(nums, target)
print(f'output: {output}')
