from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        '''
        We first get the frequency of each num in the list
        Next, we can use a min heap and for each element in the heap, we have a tuple consisting of 2 values (frequency, num)
        the heap will be sorted based on the first value of the tuple
        each time we push an element in, we also check if the size of the heap exceeds k and if so, we do a heappop
        '''
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1

        min_heap = []
        for num, frequency in freq.items():
            heappush(min_heap, (frequency, num))
            if len(min_heap) > k:
                heappop(min_heap)

        result = []
        while min_heap:
            _, num = heappop(min_heap)
            result.append(num)
        return result


sol = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
output = sol.topKFrequent(nums, k)
print(f'output: {output}')
