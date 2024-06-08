class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        if n == 1:
          return result

        for _ in range(n - 1):
          prev_char = result[0]
          count = 0
          tmp = ''

          for char in result:

            if char == prev_char:
              count += 1
            else:
              tmp += str(count) + prev_char
              count = 1
              prev_char = char
          
          tmp += str(count) + prev_char
          result = tmp

        return result
        
sol = Solution()
print(sol.countAndSay(5))