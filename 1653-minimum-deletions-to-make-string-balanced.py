class Solution:
  def minimumDeletions(self, s: str) -> int:
    '''
    Brute force
    Go through each index, and check how many 'b' on the left and how many 'a' on the right of it
    add up that and that will be the number of deletions
    Keep a variable so we try to find the minimum number of deletions
    
    We probably need some kind of cache so we don't need to re-calculate
    When we are at index 0, we make a calculation of number of 'a's after it, we also know what character this is.
    Next we proceed to index 1. We know the previous character at index 0.
      if that character is a 'b', add 1 to the total number of 'b's
    if current character is an 'a', subtract 1 to the total number of 'a's
      
    We will have 2 variables: cur_left_b, cur_right_a
    '''
    res = float('inf')
    cur_left_b = cur_right_a = 0
    # preprocess to get the number of 'a's and 'b's
    for c in s:
      cur_right_a += 1 if c == 'a' else 0

    for c in s:
      if c == 'a':
        cur_right_a -= 1
      res = min(res, cur_left_b + cur_right_a)
      if c == 'b':
          cur_left_b += 1

    return res

sol = Solution()
# s = 'aaababbab'
s = 'bbaaaaabb'
print(f'output: {sol.minimumDeletions(s)}')