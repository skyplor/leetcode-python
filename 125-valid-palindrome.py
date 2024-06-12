class Solution:
  def isPalindrome(self, s: str) -> str:
    left = 0
    right = len(s) - 1
    while left < right:
      left_char = s[left]
      right_char = s[right]
      if left_char.isalnum() and right_char.isalnum():
        left_char = left_char.lower()
        right_char = right_char.lower()
        if left_char != right_char:
          return False
        left += 1
        right -= 1
      else:
        if not left_char.isalnum():
          left += 1
        if not right_char.isalnum():
          right -= 1

    return True

sol = Solution()
# input = 'A man, a plan, a canal: Panama'
input = ",,,,,,,,,,,,acva"
output = sol.isPalindrome(input)
print(f'Input: {input}, Output: {output}')