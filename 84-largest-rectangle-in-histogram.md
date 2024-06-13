# 84. Largest Rectangle in Histogram
_hard_

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return _the area of the largest rectangle in the histogram_.


### Example 1:
![image](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

<pre>
<b>Input:</b> heights = [2,1,5,6,2,3]
<b>Output: </b>10
<b>Explanation:</b> The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
</pre>

### Example 2:
![image](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

<pre>
<b>Input:</b> heights = [2,4]
<b>Output:</b> 4
</pre>

### Constraints:

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`