from trienode import TrieNode, drawTrie
from typing import List, Optional


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        Using a Trie data structure to store the words. Then while going through the board, we use DFS to check if the word is in the Trie.
        '''
        ROWS = len(board)
        COLS = len(board[0])

        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                node.refs += 1

            node.endOfWord = True

        result = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()

        def dfs(i: int, j: int, node: Optional[TrieNode], current_word: str) -> None:
            if node.endOfWord:
                result.add(current_word)
                node.endOfWord = False  # Mark as found to avoid duplicates

                # Update reference counts along the path
                temp_node = root
                temp_node.refs -= 1
                for char in current_word:
                    temp_node = temp_node.children[char]
                    temp_node.refs -= 1

            # Early termination: if no more words can be found from this node
            if node.refs <= 0:
                return

            for dr, dc in directions:
                new_r, new_c = i + dr, j + dc
                cell = (new_r, new_c)
                if new_r in range(ROWS) and new_c in range(COLS) and cell not in seen and board[new_r][new_c] in node.children:
                    char = board[new_r][new_c]
                    child_node = node.children[char]
                    # Skip if this subtree has no valid words left
                    if child_node.refs <= 0:
                        continue
                    seen.add(cell)
                    dfs(new_r, new_c,
                        child_node, current_word+char)
                    seen.remove(cell)

        for i in range(ROWS):
            for j in range(COLS):
                char = board[i][j]
                if char in root.children:
                    seen.add((i, j))
                    dfs(i, j, root.children[char], char)
                    seen.remove((i, j))

        return list(result)


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
