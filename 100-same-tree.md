# 100. Same Tree
_easy_

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


### Example 1:
![image](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

<pre>
<b>Input:</b> p = [1,2,3], q = [1,2,3]
<b>Output:</b> true
</pre>

### Example 2:
![image](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

<pre>
<b>Input:</b> p = [1,2], q = [1,null,2]
<b>Output:</b> false
</pre>

### Example 3:
![image](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

<pre>
<b>Input:</b> p = [1,2,1], q = [1,1,2]
<b>Output:</b> false
</pre>


### Constraints:

- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`