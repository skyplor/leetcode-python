# 543. Diameter of Binary Tree
_easy_

Given the `root` of a binary tree, return _the length of the **diameter** of the tree_.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.


### Example 1:
![image](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

<pre>
<b>Input:</b> root = [1,2,3,4,5]
<b>Output:</b> 3
<b>Explanation:</b> 3 is the length of the path [4,2,1,3] or [5,2,1,3].
</pre>

### Example 2:

<pre>
<b>Input:</b> root = [1,2]
<b>Output:</b> 1
</pre>

### Constraints:

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`