from trienode import TrieNode


class Trie:
    '''
    Each node will have 2 variables: children hash and whether it is the end of the word
    Children hash will be a hash with the character as the key and the node as the value
    When we insert, we will go through each character of the word, then each time check if the character exist as the children of the current node
    if no, create the new node with the character in the children hash of the current node
    next we move the node pointer to the children's node and check again
    at the end, we set the endOfWord to True
    
    for searching, we will go through each character of the word. Anytime the character doesn't exist, we return false.
    if character exist, we move the pointer to the child node and proceed
    at the end, we check if the node is an endOfWord. and return the result
    
    for startsWith, it's the same, but at the end we just return True and no need to check for endOfWord
    '''
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
