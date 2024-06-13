from typing import List

class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    # we use a stack which stores index and height
    # we also have a max_area variable
    # using a loop
    # we push the first index and height into stack
    # next element, if height is greater than top of stack, push it in
    # if height is lesser, calculate max area of the element at top of stack and update if necessary.
    # pop the stack
    # continue popping the stack if needed (keeping track of how many is popped)
    # add this element into stack, put the index as the current_index - popped_elements
    # at the end, loop through the stack again and calculate the maximum area for each element from index till end of histogram
    stack = []
    max_area = 0
    for i, h in enumerate(heights):
      start = i
      while stack and stack[-1][1] > h:
        top_i, top_h = stack.pop()
        max_area = max(max_area, (i - top_i) * top_h)
        start = top_i

      stack.append((start, h))
    
    max_i = len(heights)
    for i, h in stack:
      max_area = max(max_area, (max_i - i) * h)
      
    return max_area

sol = Solution()
# heights = [2,1,5,6,2,3]
heights = [3,6,5,7,4,8,1,0]
# heights = [2,4]
output = sol.largestRectangleArea(heights)
print(f'heights: {heights}\nOutput: {output}')