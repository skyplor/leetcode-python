class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        '''
        We go through each word, starting from index 1.
        We will have a prev_sorted and curr_sorted 
            - If the 2 strings are equal, we mark the curr index as the index to use
            - Else, we add the word pointed to by the curr index into the result array and set the prev_sorted as the curr_sorted 
        '''
        result = []
        prev_sorted = sorted(words[0])
        i = 1
        n = len(words)
        index_to_add = 0
        while i < n:
            curr_sorted = sorted(words[i])
            if prev_sorted != curr_sorted:
                result.append(words[index_to_add])
                index_to_add = i

            i += 1
            prev_sorted = curr_sorted

        result.append(words[index_to_add])

        return result


sol = Solution()
print(
    f'output: {sol.removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"])}, expected: ["abba", "cd"]')
print(
    f'output: {sol.removeAnagrams(["a", "b", "c", "d", "e"])}, expected: ["a","b","c","d","e"]')
