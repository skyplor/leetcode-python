from typing import List

class Solution:
  def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
    # Solution 1
    '''
    for loops, get the minimum of each row, check if this is the maximum of the column and add into res set if yes
    '''
    # rowsMin = {}
    # colsMax = {}
    # for row in range(len(matrix)):
    #   rowsMin[row] = min(matrix[row])

    #   for col in range(len(matrix[row])):
    #     cell = matrix[row][col]
    #     colsMax[col] = max(colsMax[col], cell) if col in colsMax else cell

    # return [value for value in rowsMin.values() if value in colsMax.values()]
  
    # Solution 2
    minRow = {min(r) for r in matrix}
    '''
    `zip` Function
      - The zip function takes multiple iterable arguments (such as lists) and returns an iterator that aggregates elements from each of the iterables.
      - The zip function pairs up the elements from the provided iterables based on their positions.
    
    Unpacking Operator `*`
      - The unpacking operator * is used to unpack the elements of a list or any iterable.
      - When used in the context of a function call, it passes all the elements of the iterable as separate arguments to the function.
      - *matrix will unpack matrix into individual rows [1, 2, 3], [4, 5, 6], [7, 8, 9]
    
    So we are doing this: 
      - zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
      - which returns [(1,4,7), (2,5,8), (3,6,9)]
    '''
    maxCol = {max(c) for c in zip(*matrix)}
    return list(minRow & maxCol)

sol = Solution()
# matrix = [[3,7,8],[9,11,13],[15,16,17]]
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(f'output: {sol.luckyNumbers(matrix)}')