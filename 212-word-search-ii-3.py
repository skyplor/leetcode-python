class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        ROWS, COLS = len(board), len(board[0])
        trie = {}

        for w in words:
            node = trie
            for c in w:
                node = node.setdefault(c, {})
            node['#'] = w  # Use a special marker for end of word

        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, node):
            c = board[i][j]
            if c not in node:
                return

            nxt = node[c]

            # Check if we found a complete word
            if '#' in nxt:
                res.append(nxt['#'])
                del nxt['#']  # Remove found word immediately

            # Mark current cell as visited
            board[i][j] = '#'

            # Explore all 4 directions
            for dr, dc in directions:
                new_row, new_col = i + dr, j + dc
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and board[new_row][new_col] != '#':
                    dfs(new_row, new_col, nxt)

            # Restore the cell
            board[i][j] = c

            # Prune empty branches
            if not nxt:
                del node[c]

        # Start DFS from each cell
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, trie)

        return res


sol = Solution()
# board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
#          ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
# words = ["oath", "pea", "eat", "rain"]
# board = [["a","b"],["c","d"]]
# words = ["abcb"]
board = [["a"]]
words = ["a"]
output = sol.findWords(board, words)
print(f'board: {board}\nwords: {words}\noutput: {output}')
