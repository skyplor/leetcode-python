from trienode import TrieNode

class Trie:

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    current = self.root
    for c in word:
      if c not in current.children:
        current.children[c] = TrieNode()
      current = current.children[c]

    current.endOfWord = True

  def search(self, word: str) -> bool:
    current = self.root
    for c in word:
      if c not in current.children:
        return False
      current = current.children[c]
      
    return current.endOfWord

  def startsWith(self, prefix: str) -> bool:
    current = self.root
    for c in prefix:
      if c not in current.children:
        return False
      current = current.children[c]
      
    return True
      
trie = Trie()
trie.insert('apple')
print("Inserted 'apple'")
print(trie.search('apple'))
print(trie.search('app'))
print(trie.startsWith('app'))
trie.insert('app')
print("Inserted 'app'")
print(trie.search('app'))