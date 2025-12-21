from heapq import heappop, heappush, heapify


class Solution:
    def halveArray(self, nums: list[int]) -> int:
        '''
        We can use the greedy approach here by halving the largest number each time to get the minimum number of operations
        We will have an `operations` variable to keep track
        First, we calculate what is the total and the target sum
        We then put all the numbers into a heap.
        We can use a max heap that will return the next largest number each time we pop from it (To use max heap, we will need to multiply the number by -1 before pushing it)
        We then half the number and push it back into the heap, keeping track of the current sum by subtracting the target sum by the halved amount
        If the target sum <= 0, we can return the operations
        '''
        operations = 0
        heap = [-n for n in nums]
        target_sum = sum(nums) / 2
        heapify(heap)

        while target_sum > 0:
            current_num = -heappop(heap)
            new_num = current_num / 2
            target_sum -= (current_num - new_num)
            heappush(heap, -new_num)
            operations += 1

        return operations


sol = Solution()
nums = [5, 19, 8, 1]
output = sol.halveArray(nums)
print(f'output: {output}')
