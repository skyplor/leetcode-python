class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
          return False

        dict = {}
        for char in s:
          dict[char] = dict.get(char, 0) + 1
        
        for char in t:
          if char not in dict:
            return False
          occurrence = t.count(char)
          prev_count = dict[char]
          if occurrence != prev_count:
            return False
        return True
sol = Solution()
print(sol.isAnagram('anagram', 'nigaram'))