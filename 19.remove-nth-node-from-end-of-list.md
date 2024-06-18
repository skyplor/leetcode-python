# 19. Remove Nth Node From End of List
_medium_

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.


### Example 1:
![image](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

<pre>
<b>Input:</b> head = [1,2,3,4,5], n = 2
<b>Output:</b> [1,2,3,5]
</pre>

### Example 2:

<pre>
<b>Input:</b> head = [1], n = 1
<b>Output:</b> []
</pre>

### Example 3:

<pre>
<b>Input:</b> head = [1,2], n = 1
<b>Output:</b> [1]
</pre>

### Constraints:

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`