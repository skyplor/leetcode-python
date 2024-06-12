# See: https://youtu.be/UbyhOgBN834?t=623
class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2): return False
    length = len(s1)
    alphabet_count = 26
    s1_count, s2_count = [0] * alphabet_count, [0] * alphabet_count
    matches = 0
    l, r = 0, length - 1
    for c in s1:
      s1_count[ord(c) - ord('a')] += 1
    for c in s2[l:r + 1]:
      s2_count[ord(c) - ord('a')] += 1
    for i in range(alphabet_count):
      matches += (1 if s1_count[i] == s2_count[i] else 0)

    while r < len(s2):
      if matches == alphabet_count:
        return True

      if l > 0:
        prev_char = s2[l - 1]
        new_char = s2[r]
        index = ord(prev_char) - ord('a')
        s2_count[index] -= 1
        if s1_count[index] == s2_count[index]:
          matches += 1
        elif s1_count[index] - 1 == s2_count[index]:
          matches -= 1

        index = ord(new_char) - ord('a')
        s2_count[index] += 1
        if s1_count[index] == s2_count[index]:
          matches += 1
        elif s1_count[index] + 1 == s2_count[index]:
          matches -= 1
      l += 1
      r += 1

    return matches == alphabet_count

sol = Solution()
s1 = 'abc'
s2 = 'bbbca'
output = sol.checkInclusion(s1, s2)
print(f's1: {s1}\ns2: {s2}\nOutput: {output}')