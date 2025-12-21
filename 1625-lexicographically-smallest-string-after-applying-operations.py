class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        '''
        We can use BFS to brute force this because the total number of operations for brute force is O(n * 10 * n)
        Since n has a max of value 100, we can safely brute force since it will only be a maximum of 10^6

        Logic:
            - We have a set that keeps track of ALL string combinations we have seen so far.
            - We have a res string that stores the Lexicographically smallest string seen (initialised to `s`)
            - We have a queue that stores strings to be processed
            - We have a while loop that continues as long as the queue is not empty
            - At each iteration, we pop the first string,
                - do `add` operation
                    - if the new string hasn't been seen before, add into `seen` set and add into `queue`
                    - compare with `res` and update if this new string is smaller
                - do `rotate` operation
                    - if the new string hasn't been seen before, add into `seen` set and into `queue`
                    - compare with `res` and update if this new string is smaller

        '''
        res = s
        seen = set()
        queue = [s]

        def perform_add(cur: str) -> str:
            for i in range(1, len(s), 2):
                new_char = chr((ord(cur[i]) - ord('0') + a) % 10 + ord('0'))
                cur = cur[0:i] + new_char + cur[i+1:]

            return cur

        def perform_rotate(cur: str) -> str:
            n = len(cur)
            return cur[n-b:] + cur[0:n-b]

        def find_smaller_s(x: str, y: str) -> str:
            return x if x < y else y

        def check_and_update(new_string: str):
            nonlocal res

            if new_string not in seen:
                seen.add(new_string)
                queue.append(new_string)
                res = find_smaller_s(res, new_string)

        while queue:
            cur = queue.pop()

            added_string = perform_add(cur)
            check_and_update(added_string)

            rotated_string = perform_rotate(cur)
            check_and_update(rotated_string)

        return res


sol = Solution()
print(f'output: {sol.findLexSmallestString('5525', 9, 2)}, expected: 2050')
