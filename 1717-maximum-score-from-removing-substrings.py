class Solution:
  def maximumGain(self, s: str, x: int, y: int) -> int:
    # Recursion
    # memo = {}

    # def recurseGain(curS):
    #   if curS in memo:
    #     return memo[curS]
    #   if curS.count('ab') == 1 and curS.count('ba') == 0:
    #     memo[curS] = x
    #     return x
    #   if curS.count('ba') == 1 and curS.count('ab') == 0:
    #     memo[curS] = y
    #     return y

    #   ab_res = 0
    #   ba_res = 0

    #   if 'ab' in curS:
    #     replaced_ab = curS.replace('ab', '', 1)
    #     ab_res = recurseGain(replaced_ab) + x
    #   if 'ba' in curS:
    #     replaced_ba = curS.replace('ba', '', 1)
    #     ba_res = recurseGain(replaced_ba) + y

    #   val = max(ab_res, ba_res)
    #   memo[curS] = val
    #   return val
    # return recurseGain(s)

    # Greedy
    # Time: O(n)
    # Space: O(n)
    '''
    will need to find max(x, y)
    removing a string can affect the rest of the string
    e.g abab -> remove 'ba' will introduce 'ab'
    '''
    # def remove_pairs(pair, score):
    #   nonlocal s
    #   temp_res = 0
    #   stack = []

    #   for c in s:
    #     if c == pair[1] and stack and stack[-1] == pair[0]:
    #       stack.pop()
    #       temp_res += score
    #     else:
    #       stack.append(c)
    #   s = "".join(stack)
    #   return temp_res
    # res = 0
    # pair = 'ab' if x > y else 'ba'

    # res += remove_pairs(pair, max(x, y))
    # res += remove_pairs(pair[::-1], min(x, y))
    # return res

    # Greedy
    # Time: O(n)
    # Space: O(1)
    a_count = 0
    b_count = 0
    lesser = min(x, y)
    result = 0

    for c in s:
        if c > 'b':
            result += min(a_count, b_count) * lesser
            a_count = 0
            b_count = 0
        elif c == 'a':
            if x < y and b_count > 0:
                b_count -= 1
                result += y
            else:
                a_count += 1
        elif c == 'b':
            if x > y and a_count > 0:
                a_count -= 1
                result += x
            else:
                b_count += 1

    result += min(a_count, b_count) * lesser
    return result

sol = Solution()
s = "cdbcbbaaabab"
x = 4
y = 5
# s = "aabbaaxybbaabb"
# x = 5
# y = 4
# s = "aabbrtababbabmaaaeaabeawmvaataabnaabbaaaybbbaabbabbbjpjaabbtabbxaaavsmmnblbbabaeuasvababjbbabbabbasxbbtgbrbbajeabbbfbarbagha"
# x = 8484
# y = 4096
print(f'output: {sol.maximumGain(s, x, y)}')