# 23. Merge k Sorted Lists
_hard_

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

_Merge all the linked-lists into one sorted linked-list and return it._


### Example 1:

<pre>
<b>Input:</b> lists = [[1,4,5],[1,3,4],[2,6]]
<b>Output:</b> [1,1,2,3,4,4,5,6]
<b>Explanation:</b> The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
</pre>

### Example 2:

<pre>
<b>Input:</b> lists = []
<b>Output:</b> []
</pre>

### Example 3:

<pre>
<b>Input:</b> lists = [[]]
<b>Output:</b> []
</pre>

### Constraints:

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in **ascending order**.
- The sum of `lists[i].length` will not exceed `10^4`.