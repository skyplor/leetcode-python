# 21. Merge Two Sorted Lists
_easy_

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return _the head of the merged linked list_.

### Example 1:
![image](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

<pre>
<b>Input:</b> list1 = [1, 2, 4], list2 = [1, 3, 4]
<b>Output:</b> [1, 1, 2, 3, 4, 4]
</pre>

### Example 2:

<pre>
<b>Input:</b> list1 = [], list2 = []
<b>Output:</b> []
</pre>

### Example 3:

<pre>
<b>Input:</b> list1 = [], list2 = [0]
<b>Output:</b> [0]
</pre>

### Constraints:

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.
