from typing import List
from heapq import heappush, heappop
from collections import Counter

class Solution:
  def frequencySort(self, nums: List[int]) -> List[int]:
    # Solution 1:
    # '''
    # 2 hashmaps:
    # - h1 = {num: frequency}
    # - h2 = {frequency: maxHeap(-num)}
    
    # get the keys = sorted(h2.keys())
    # loop through the sorted keys and get the nums -> make sure we negate the num and add X instances of num into the res
    # '''
    
    # num_count = {}
    # frequency_heap = {}
    # res = []
    # for num in nums:
    #   if num not in num_count:
    #     num_count[num] = 0

    #   prev_frequency = num_count[num]
    #   new_frequency = prev_frequency + 1
    #   num_count[num] = new_frequency
    #   if prev_frequency not in frequency_heap:
    #     if new_frequency not in frequency_heap:
    #       frequency_heap[new_frequency] = set()
    #     frequency_heap[new_frequency].add(-num)
    #   else:
    #     prev = frequency_heap[prev_frequency]
    #     if -num in prev:
    #       prev.remove(-num)
    #     if new_frequency not in frequency_heap:
    #       frequency_heap[new_frequency] = set()
    #     frequency_heap[new_frequency].add(-num)
    # keys = sorted(frequency_heap.keys())
    # for key in keys:
    #   nums_set = frequency_heap[key]
    #   max_heap = []
    #   for num in nums_set:
    #     heappush(max_heap, num)
    #   for _ in nums_set:
    #     negated_num = heappop(max_heap)
    #     num = -negated_num
    #     freq = num_count[num]
    #     for _ in range(freq):
    #       res.append(num)
          
    # return res
    
    # Solution 2:
    '''
    use collections Counter and sorted function by providing a key to sort it by
    '''
    nums_count = Counter(nums)
    sorted_key = lambda x: (nums_count[x], -x)
    return sorted(nums, key=sorted_key)

sol = Solution()
# nums = [1,1,2,2,2,3]
# nums = [2,3,1,3,2]
nums = [-1,1,-6,4,5,-6,1,4,1]
print(f'output: {sol.frequencySort(nums)}')