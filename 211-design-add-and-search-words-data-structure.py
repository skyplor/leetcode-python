from trienode import TrieNode

class WordDictionary:

  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word: str) -> None:
    current = self.root
    for c in word:
      if c not in current.children:
        current.children[c] = TrieNode()

      current = current.children[c]
      
    current.endOfWord = True

  def search(self, word: str) -> bool:
    def dfs(index, root):
      current = root
      for i in range(index, len(word)):
        c = word[i]

        if c == '.':
          for child in current.children.values():
            if dfs(i + 1, child):
              return True
          return False
        else:
          if c not in current.children:
            return False
          current = current.children[c]
          
      return current.endOfWord

    return dfs(0, self.root)
  
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))