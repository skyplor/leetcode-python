class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        for c in s:
          s_count[c] = 1 + s_count.get(c, 0)
        
        for c in t:
          if c not in s_count or s_count[c] < 1: return False
          s_count[c] -= 1
          
        return all(val == 0 for val in s_count.values())
sol = Solution()
print(sol.isAnagram('anagram', 'nigaram'))
print(sol.isAnagram('anagram', 'nagaram'))