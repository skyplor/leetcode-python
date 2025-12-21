# 110. Balanced Binary Tree
_easy_

Given a binary tree, determine if it is **height-balanced**.

**Note**: a height-balanced binary tree is defined as:
  - a binary tree in which the left and right subtrees of every node differ in height by no more than 1

### Example 1:
![image](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

<pre>
<b>Input:</b> root = [3,9,20,null,null,15,7]
<b>Output:</b> true
</pre>

### Example 2:
![image](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

<pre>
<b>Input:</b> root = [1,2,2,3,3,null,null,4,4]
<b>Output:</b> false
</pre>

### Example 3:

<pre>
<b>Input:</b> root = []
<b>Output:</b> true
</pre>


### Constraints:

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`