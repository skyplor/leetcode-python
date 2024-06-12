from collections import Counter

class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    # length of s1 will be the window size
    # dictionary of character counts of s1.
    # for each window of s2, create a new dictionary of character counts of s2 and compare against s1. if equal, output true
    # if not equal, move the window +1
    length = len(s1)
    s1_count = Counter(s1)
    l, r = 0, length - 1
    s2_count = Counter(s2[l:r+1])
    while r < len(s2):
      if l > 0:
        prev_char = s2[l - 1]
        new_char = s2[r]
        prev_char_count =  s2_count.get(prev_char, 0)
        if prev_char_count > 1:
          s2_count[prev_char] -= 1
        elif prev_char_count == 1:
          del s2_count[prev_char]

        s2_count[new_char] = s2_count.get(new_char, 0) + 1

      if s2_count == s1_count:
        return True
      l += 1
      r += 1

    return False

sol = Solution()
s1 = 'adc'
s2 = 'dcda'
output = sol.checkInclusion(s1, s2)
print(f's1: {s1}\ns2: {s2}\nOutput: {output}')