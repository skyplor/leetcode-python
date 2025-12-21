class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import Counter
        '''
        1. create a count of the characters. Since we have only 26 characters, we can have a list of length 26 and value will be the character count
        2. enumerate through each char of s, for each iteration, append c into t and then do Operation 1
        3. Operation 1: peek at the t, is there any other character smaller than t? if no, do Operation 2, otherwise, continue
        4. Operation 2: pop from t and append to p
        '''

        char_count = Counter(s)
        t = []
        p = []

        def min_char():
            for i in range(26):
                char = chr(ord('a')+i)
                if char_count[char] > 0:
                    return char

            return 'a'

        def operation_one(c: str):
            t.append(c)
            char_count[c] -= 1

        def operation_two():
            while t and t[-1] <= min_char():
                p.append(t.pop())

        for c in s:
            operation_one(c)
            operation_two()

        while t:
            p.append(t.pop())

        return "".join(p)


sol = Solution()
# s = "zza"
# s = "bac"
# s = "bdda"
s = "bydevfziy"
output = sol.robotWithString(s)
print(f"s: {s}, output: {output}")
