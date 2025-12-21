class Solution:
    def compress(self, chars: list[str]) -> int:
        '''
        We have a read and write pointers
        we also have a count pointer to store the current number of char
        we also have a current_char pointer to store the char we are currently counting
        go through the chars, have the read and write pointer start at first element. 
        if the char at read pointer == current_char, we add 1 to count pointer and move read pointer forward.
        else, we can proceed to write the current_char, then move the write pointer to next, and write the current count, then move the write pointer forward again
        then we update count pointer back to 0 and update current_char to the char pointed by read pointer
        '''
        write = 0
        count = 0
        c = chars[0]
        for read in range(len(chars)):
            cur = chars[read]
            if cur == c:
                count += 1
                continue
            chars[write] = c
            write += 1

            if count > 1:
                count_str = str(count)
                for ch in count_str:
                    chars[write] = ch
                    write += 1
            # reset count and set c to cur
            count = 1
            c = cur

        chars[write] = c
        write += 1

        if count > 1:
            count_str = str(count)
            for ch in count_str:
                chars[write] = ch
                write += 1
        return write


sol = Solution()
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
output = sol.compress(chars)
print(f"chars: {chars}\noutput: {output}")
