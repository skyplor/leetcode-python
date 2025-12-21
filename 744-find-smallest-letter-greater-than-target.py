class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        '''
        We use binary search for this and compare the characters directly. instead of returning directly if mid == target,
        since we need to return the character that is larger than target, we simply move the pointers,
        we just move the left and right pointers accordingly and at the end return the left pointer
        '''
        left, right = 0, len(letters)
        while left < right:
            mid = left + (right - left) // 2
            if target < letters[mid]:
                right = mid
            else:
                left = mid + 1

        return letters[left % len(letters)]


sol = Solution()
letters = ['c', 'f', 'j']
# target = 'a'
target = 'g'
output = sol.nextGreatestLetter(letters, target)
print(f'output: {output}')
