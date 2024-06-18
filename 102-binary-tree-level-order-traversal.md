# 102. Binary Tree Level Order Traversal
_medium_

Given the `root` of a binary tree, return _the level order traversal of its nodes' values._ (i.e., from left to right, level by level).

### Example 1:
![image](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
<pre>
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
</pre>

### Example 2:

<pre>
Input: root = [1]
Output: [[1]]
</pre>

### Example 3:

<pre>
Input: root = []
Output: []
</pre>

### Constraints:

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`