# 287. Find the Duplicate Number
_medium_

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return _this repeated number_.

You must solve the problem **without** modifying the array `nums` and uses only constant extra space.


### Example 1:

<pre>
<b>Input:</b> nums = [1,3,4,2,2]
<b>Output:</b> 2
</pre>

### Example 2:

<pre>
<b>Input:</b> nums = [3,1,3,4,2]
<b>Output:</b> 3
</pre>

### Example 3:

<pre>
<b>Input:</b> nums = [3,3,3,3,3]
<b>Output:</b> 3
</pre>

### Constraints:

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more times**.

### Follow up:

- How can we prove that at least one duplicate number must exist in `nums`?
- Can you solve the problem in linear runtime complexity?