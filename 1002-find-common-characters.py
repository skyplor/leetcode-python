from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # {'c': 1, 'o': 2, 'l': 1}
        # get all the keys, calculate the number of times the key appear in the new word. If less than the current value, update the current value
        tempResult = {}
        result = []
        firstWord = words[0]
        for c in firstWord:
          tempResult[c] = tempResult.get(c, 0) + 1

        for word in words:
          for key in tempResult.keys():
            occurrence = word.count(key)
            prev_count = tempResult[key]
            if occurrence < prev_count:
              tempResult[key] = occurrence
        for k, v in tempResult.items():
          if v > 0:
            result.extend([k]*v)

        return result
sol = Solution()
print(sol.commonChars(["cool","lock","cook"]))