from typing import List

class Solution:
  def encode(self, strs: List[str]) -> str:
    # if we join all the strings together, we won't know where to break them when decoding
    # if we add a delimiter, we won't know if this delimiter will appear in the actual string as well
    # we can include the length of each string while encoding so during decoding we know
    # again, if this number is also in the string, we might mistaken it as the length of the next string, so we add a delimiter for it
    result = ''
    delimiter = '#'
    for string in strs:
      result += str(len(string)) + delimiter + string
    return result
  
  def decode(self, s: str) -> List[str]:
    # E.g 4#This2#is1#a6#string
    result = []
    i = 0
    start_idx = -1
    while i < len(s):
      c = s[i]
      if c.isnumeric():
        if start_idx == -1:
          start_idx = i
        i += 1
      elif c == '#':
        if start_idx > -1:
          length = int(s[start_idx:i])
          next_i = i + 1 + length
          substring = s[i+1:next_i]
          if substring is not None:
            result.append(substring)
            start_idx = -1
                
          i = next_i
        else:
          i += 1

    return result
  
sol = Solution()
input = ['This', 'is', 'a', 'string']
encoded = sol.encode(input)
output = sol.decode(encoded)
print(f'Input: {input}, Encoded: {encoded}, Output: {output}')