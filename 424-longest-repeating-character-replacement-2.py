class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    count = {}
    l = 0
    res = 0
    max_f = 0

    for r in range(len(s)):
      count[s[r]] = 1 + count.get(s[r], 0)
      max_f = max(max_f, count[s[r]])
      while (r - l + 1) - max_f > k:
        count[s[l]] -= 1
        l += 1
      res = max(res, r - l + 1)

    return res

sol = Solution()
# s = 'ABAB'
# s = 'AABABBA'
s = 'ABBB'
k = 2
output = sol.characterReplacement(s, k)
print(f'S: {s}\nK: {k}\nOutput: {output}')