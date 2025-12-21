class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        split `s` by space, then remove empty list item from the list
        using 2 pointers to swap left and right words until the left > right
        return the swapped result joined by space
        '''
        result = s.split(None)
        left, right = 0, len(result) - 1
        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        return ' '.join(result)


sol = Solution()
# s = '   the    sky is blue'
s = "a good   example"
output = sol.reverseWords(s)
print(f'output: {output}')
