class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
          return "1"

        prev = self.countAndSay(n-1)
        result = ''

        count = 1
        prev_char = prev[0]
        for i in range(1, len(prev)):
          digit = prev[i]

          if digit == prev_char:
            count += 1
          else:
            result += str(count) + prev_char
            count = 1
            prev_char = digit
          
        result += str(count) + prev_char

        return result
        
sol = Solution()
print(sol.countAndSay(5))