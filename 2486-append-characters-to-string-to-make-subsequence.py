class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
      # 2 ptrs for s and t
      ptr_s, ptr_t = 0, 0
      while ptr_s < len(s) and ptr_t < len(t):
        if s[ptr_s] == t[ptr_t]:
          ptr_t += 1

        ptr_s += 1

      return len(t) - ptr_t

sol = Solution()
print(sol.appendCharacters('z', 'abcd'))
