class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        we have 2 pointers (left and right)
        we also have 2 hashes, 1 for t and 1 for the window
        we also have 2 variables that we will use to check if the condition has been met (check_window and check_t)
        check_t is the length of the keys in t hash
        check_window is the number of keys in window hash that matches the count of the corresponding key in t hash
        we will take note of the count for a key in the window hash and in t hash. if the count match exactly, we increment the check_window
        if the count changes from matching to less than, then we decrement the check_window
        if check_window and check_t matches, that means we have found a match and we get the 2 indices (left & right) and update result if it is smaller than current result
        '''
        if s == '':
            return ''

        t_hash = {}
        for c in t:
            t_hash[c] = 1 + t_hash.get(c, 0)

        window_hash = {}
        check_t = len(t_hash)
        check_window = 0
        res, res_len = [-1, -1], float('inf')

        left = 0
        for right in range(len(s)):
            char = s[right]
            window_hash[char] = 1 + window_hash.get(char, 0)

            if char in t_hash and window_hash[char] == t_hash[char]:
                check_window += 1

            while check_window == check_t:
                current_length = right - left + 1
                if current_length < res_len:
                    res = [left, right]
                    res_len = current_length

                left_char = s[left]
                window_hash[left_char] -= 1
                if left_char in t_hash and window_hash[left_char] < t_hash[left_char]:
                    check_window -= 1
                left += 1

        left, right = res
        return s[left:right+1] if res_len != float('inf') else ''


sol = Solution()
s = 'aa'
t = 'aa'
output = sol.minWindow(s, t)
print(f's: {s}\nt: {t}\nOutput: {output}')
