class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def __repr__(self):
        return 'TrieNode(children: {}, endOfWord: {})'.format(self.children, self.endOfWord)
