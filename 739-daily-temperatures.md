# 739. Daily Temperatures
_medium_

Given an array of integers `temperatures` represents the daily temperatures, return _an array_ `answer` _such that_ `answer[i]` _is the number of days you have to wait after the_ `ith` _day to get a warmer temperature_. If there is no future day for which this is possible, keep `answer[i] == 0` instead.


### Example 1:

<pre>
<b>Input:</b> temperatures = [73,74,75,71,69,72,76,73]
<b>Output:</b> [1,1,4,2,1,1,0,0]
</pre>

### Example 2:

<pre>
<b>Input:</b> temperatures = [30,40,50,60]
<b>Output:</b> [1,1,1,0]
</pre>

### Example 3:

<pre>
<b>Input:</b> temperatures = [30,60,90]
<b>Output:</b> [1,1,0]
</pre>


### Constraints:

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`