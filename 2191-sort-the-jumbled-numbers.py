from typing import List

class Solution:
  def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
    # Solution 1(not so optimal):
    '''
    calculate mapped value for each num
    store mapped value
    1 hashmap:
    - h = {mapped_value: array_of_nums}
    
    sorted keys and append all into res array
    '''
  
    # def calculate_mapped_value(num: int) -> int:
    #   string_num = str(num)
    #   converted_str = ''
    #   for c in string_num:
    #     converted_str += str(mapping[int(c)])

    #   return int(converted_str)

    # converted_mapping = {}
    # for num in nums:
    #   mapped_value = calculate_mapped_value(num)
    #   if mapped_value not in converted_mapping:
    #     converted_mapping[mapped_value] = []
        
    #   converted_mapping[mapped_value].append(num)
      
    # sorted_keys = sorted(converted_mapping.keys())
    # res = []
    # for key in sorted_keys:
    #   for i in converted_mapping[key]:
    #     res.append(i)
      
    # return res
  
    # Solution 2 (optimal): 
    def calculate_mapped_value(num: int) -> int:
      if num == 0:
          return mapping[0]
      n, f = 0, 1
      while num > 0:
          num, r = divmod(num, 10)
          n += mapping[r] * f
          f *= 10
      return n
    
    indices = sorted(range(len(nums)), key=lambda i: calculate_mapped_value(nums[i]))
      
    return [nums[i] for i in indices]

sol = Solution()
mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]
print(f'output: {sol.sortJumbled(mapping, nums)}')