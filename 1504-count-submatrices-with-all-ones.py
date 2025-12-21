from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        '''
        Starting from the top left corner, we go through each cell to get the number of submatrices with all ones ending at this cell as the bottom right cell
        We will solve this using an increasing monotonic stack. For each stack, we will have to track 3 values (height, col_index, prev_count)
        We will have a total_count var to track the current total count
        We also need to understand the concept of gap and height. 
        Gap:
            - The width of the rectangle we can form at the current height, considering the monotonic stack constraint.
            - It's j - col_index where col_index is from the previous element in the stack that has height < current height.
        Height:
            - how far we can go to the top of the current cell (only if this cell has a '1') when all the cells are '1's

        Formula to calculate the submatrice with this cell as the bottom right ending cell:
            (gap * height) + (prev_count)

        We will need a histogram var to keep track of the heights at each cell. 
            - For this histogram, basically it's like a tetris, we just process each row, and the next row will just add the prev row's value at the same column + 1 (if the next row same col had a '1').
            - If the next row has 0 as the col value, then we don't add up but set it as 0
        We always initialise the stack with (height, col_index, prev_count): (-1, -1, 0)
        We will reinitialise the stack for new row that we process
        '''
        ROWS = len(mat)
        COLS = len(mat[0])
        histogram = [0] * COLS
        total_count = cur_count = 0

        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 1:
                    histogram[j] += 1
                else:
                    histogram[j] = 0

            stack = [(-1, -1, 0)]
            for j in range(COLS):
                while (stack[-1][0] >= histogram[j]):
                    stack.pop()

                _, col_index, prev_count = stack[-1]
                gap = j - col_index
                cur_count = (histogram[j] * gap) + prev_count
                total_count += cur_count
                stack.append((histogram[j], j, cur_count))

        return total_count


sol = Solution()
mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
print(f'output: {sol.numSubmat(mat)}')
