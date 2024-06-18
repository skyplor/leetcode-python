from trienode import TrieNode
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        self.addWords(root, words)

        ROWS, COLS = len(board), len(board[0])

        res, visited = set(), set()

        def dfs(r, c, node, tmp_result):
            if (
                    r not in range(ROWS)
                    or c not in range(COLS)
                    or board[r][c] not in node.children
                    or (r, c) in visited):
                return

            # mark visited
            visited.add((r, c))

            node = node.children[board[r][c]]
            tmp_result += board[r][c]
            if node.endOfWord:
                node.endOfWord = False
                res.add(tmp_result)
            dfs(r + 1, c, node, tmp_result)
            dfs(r - 1, c, node, tmp_result)
            dfs(r, c + 1, node, tmp_result)
            dfs(r, c - 1, node, tmp_result)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, '')

        return list(res)

    def addWords(self, root: TrieNode, words: List[str]) -> None:
        for word in words:
            current = root
            for c in word:
                if c not in current.children:
                    current.children[c] = TrieNode()

                current = current.children[c]

            current.endOfWord = True


sol = Solution()
board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
         ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
output = sol.findWords(board, words)
print(f'board: {board}\nwords: {words}\noutput: {output}')
