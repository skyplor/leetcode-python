# 74. Search a 2D Matrix
_medium_

You are given an `m x n` integer matrix `matrix` with the following two properties:

  - Each row is sorted in non-decreasing order.
  - The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` _if `target` is in matrix or `false` otherwise_.

You must write a solution in `O(log(m * n))` time complexity.


Example 1:
![image](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

<pre>
<b>Input:</b> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
<b>Output:</b> true
</pre>

Example 2:
![image](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

<pre>
<b>Input:</b> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
<b>Output:</b> false
</pre>

### Constraints:

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`