from typing import List
from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        We build an adjacency list that connects each word to its neighbour IF it differs by a single letter
        This means we need a function that determines that
        Next, to find shortest path, we can use BFS
        For BFS, we can use a queue
        We also need a `visited` variable to keep track of visited word to prevent us from processing the same word again
        '''
        if endWord not in wordList:
            return 0

        visited = set()
        queue = deque()
        adj_list = defaultdict(list)

        # def is_valid_neighbour(w1: str, w2: str) -> bool:
        #     diff_count = 0
        #     for i in range(len(w1)):
        #         if w1[i] != w2[i]:
        #             diff_count += 1
        #         if diff_count > 1:
        #             return False

        #     return True

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj_list[pattern].append(word)

        for j in range(len(beginWord)):
            pattern = beginWord[:j] + '*' + beginWord[j+1:]
            queue.extend(adj_list[pattern])

        counter = 1
        while queue:
            print(queue)
            counter += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                visited.add(cur)

                if cur == endWord:
                    return counter

                for j in range(len(cur)):
                    pattern = cur[:j] + '*' + cur[j+1:]
                    for neighbour in adj_list[pattern]:
                        if neighbour not in visited:
                            queue.append(neighbour)

        return 0


sol = Solution()
beginWord = 'hit'
endWord = 'cog'
wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
# wordList = ['hot', 'dot', 'tog', 'cog']
output = sol.ladderLength(beginWord, endWord, wordList)
print(
    f'beginWord: {beginWord}\nendWord: {endWord}\nwordList: {wordList}\noutput: {output}')
