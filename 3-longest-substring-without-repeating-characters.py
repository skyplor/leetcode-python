class Solution:
  def lengthOfLongestSubstring(self, s: str) -> str:
    if len(s) == 0:
      return 0

    start, end = 0, 1
    longest = 1

    while end < len(s):
      current_substring = s[start:end]
      if s[end] in current_substring:
        start += 1
        end = start + 1
      else:
        end += 1
      longest = max(end - start, longest)

    return longest
  
sol = Solution()
# input = 'abcabcbb'
input = 'dvdf'
# input = ' '
output = sol.lengthOfLongestSubstring(input)
print(f'Input: {input}\nOutput: {output}')