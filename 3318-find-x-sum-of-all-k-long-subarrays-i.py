from heapq import heapify, heappop


class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        '''
        We have a loop that goes from 0 to (n - k)
        We have a variable `count` that is a map of the count of each integer
        We also have a variable `result` that stores the result
        In each loop,
            If i == 0,
                We calculate the count of all elements from i to (i + k - 1)
            else,
                we get the previous i, reduce the count for that by 1, and get i + k - 1 and increment the count for it
            Then we add all the elements into a max heap and have a for loop to retrieve the top x elements and add up the sum
            Then add it into the result array
        '''
        result = []
        count = {}
        n = len(nums)
        for i in range(n - k + 1):
            max_heap = []
            sum = 0

            if i == 0:
                for j in range(k):
                    count[nums[j]] = count.get(nums[j], 0) + 1

            else:
                prev = nums[i-1]
                next = nums[i + k - 1]
                count[prev] -= 1
                count[next] = count.get(next, 0) + 1

            for key, val in count.items():
                max_heap.append((-val, -key))

            heapify(max_heap)
            for _ in range(x):
                if max_heap:
                    neg_val, neg_key = heappop(max_heap)
                    sum += -neg_val * -neg_key
            result.append(sum)

        return result


sol = Solution()
nums = [1, 1, 2, 2, 3, 4, 2, 3]
k = 6
x = 2
print(f'output: {sol.findXSum(nums, k, x)}, expected: [6, 10, 12]')

nums = [3, 8, 7, 8, 7, 5]
k = 2
x = 2
print(f'output: {sol.findXSum(nums, k, x)}, expected: [11, 15, 15, 15, 12]')

nums = [9, 2, 2]
k = 3
x = 3
print(f'output: {sol.findXSum(nums, k, x)}, expected: [13]')
