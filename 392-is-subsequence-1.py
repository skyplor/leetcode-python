class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        We can use 2 pointers, 1 point to `s` and another point to `t`.
        Each time we compare the characters pointed to by each pointer.
        Once pointer s reach end of s, and t hasn't, that means t has the subsequence, and we can return True. But if t reaches end first, then we return False
        
        Edge case:
            - If len(s) > len(t), return False
        '''
        s_len, t_len = len(s), len(t)
        if s_len == 0:
            return True
        if s_len > t_len:
            return False
        
        p_s = p_t = 0
        while p_t < len(t):
            s_char, t_char = s[p_s], t[p_t]
            if s_char == t_char:
                p_s += 1
                p_t += 1
            else:
                p_t += 1
                
            if p_s == s_len:
                return True
            
        return False
        
sol = Solution()
s = "abc"
t = "ahbgdc"
print(f'output: {sol.isSubsequence(s, t)}, expected: true')
s = "axc"
t = "ahbgdc"
print(f'output: {sol.isSubsequence(s, t)}, expected: false')