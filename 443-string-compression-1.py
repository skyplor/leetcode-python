from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        read_index = 0
        write_index = 0
        while read_index < len(chars):
            count = 0
            char = chars[read_index]

            while read_index < len(chars) and chars[read_index] == char:
                count += 1
                read_index += 1

            chars[write_index] = char
            write_index += 1

            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        return write_index


sol = Solution()
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
output = sol.compress(chars)
print(f"chars: {chars}\noutput: {output}")
