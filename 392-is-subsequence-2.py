from collections import defaultdict


class Solution:
    def preprocess_t(self, t: str) -> dict[str, list[int]]:
        res = defaultdict(list)
        for i, c in enumerate(t):
            res[c].append(i)

        return res

    def isSubsequence(self, s: str, preprocessed_t: dict) -> bool:
        '''
        If we want to improve this such that if there are huge number of `s` strings to match against 1 `t` string
        We will preprocess t by creating a map of where each character appears in t {<char>: [<index_1>, <index_2]}
        Then we have a max_current_index variable, and go through each character in `s`
            We then use binary_search to get the first index that is bigger than the max_current_index.
            If it exists, use that and update the max_current_index. if no, return False.

        At the end of loop, return True
        '''
        def binary_search(indices: list[int], target: int) -> int:
            n = len(indices)
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if target < indices[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            if left > n - 1:
                return -1
            return indices[left]

        s_len = len(s)
        if s_len == 0:
            return True

        max_current_index = -1
        for c in s:
            list_of_idx = preprocessed_t[c]
            index_to_place = binary_search(list_of_idx, max_current_index)
            if index_to_place == -1:
                return False
            else:
                max_current_index = index_to_place

        return True


sol = Solution()
s = "abc"
t = "ahbgdc"
print(f'output: {sol.isSubsequence(s, sol.preprocess_t(t))}, expected: true')
s = "axc"
t = "ahbgdc"
print(f'output: {sol.isSubsequence(s, sol.preprocess_t(t))}, expected: false')
