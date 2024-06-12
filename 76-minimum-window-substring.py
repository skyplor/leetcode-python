class Solution:
  def minWindow(self, s: str, t:str) -> str:
    if t == '' or len(t) > len(s): return ''

    t_count = {}
    swindow_count = {}
    for c in t:
      t_count[c] = t_count.get(c, 0) + 1

    have = 0
    need = len(t_count)

    l = 0
    res, resLen = [-1, -1], float("infinity")

    for r in range(len(s)):
      c = s[r]
      swindow_count[c] = swindow_count.get(c, 0) + 1
      if c in t_count and swindow_count[c] == t_count[c]:
        have += 1
        
      while have == need:
        # update result
        if (r - l + 1) < resLen:
          res = [l, r]
          resLen = (r - l + 1)
        # remove from left of window
        swindow_count[s[l]] -= 1
        if s[l] in t_count and swindow_count[s[l]] < t_count[s[l]]:
          have -= 1
        l += 1

    l, r = res
    return s[l:r+1] if resLen != float('infinity') else ''
  
sol = Solution()
s = 'aa'
t = 'aa'
output = sol.minWindow(s, t)
print(f's: {s}\nt: {t}\nOutput: {output}')