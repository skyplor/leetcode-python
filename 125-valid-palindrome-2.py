class Solution:
  def isPalindrome(self, s: str) -> str:
    s_lower = s.lower()
    check_s = ''.join(c for c in s_lower if c.isalnum())

    return check_s == ''.join(reversed(check_s))

sol = Solution()
# input = 'A man, a plan, a canal: Panama'
input = ",,,,,,,,,,,,acva"
output = sol.isPalindrome(input)
print(f'Input: {input}, Output: {output}')