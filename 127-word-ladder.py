from typing import List
from collections import defaultdict, deque

class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    '''
    graph problem with beginword as the first node and endword as the last node
    word list contains the rest of the nodes
    We need to first build the path/edges between each node.
    This is a bidirectional graph where each node can potentially join to other nodes
    if using brute force way to build the edges, we will have O((n^2)*m)
      because we need to go through each node and each character (m) of the word
    Alternative way is to generate a list of keys from each word. Each key will have a single character replaced
    e.g hot -> '*ot', 'h*t', 'ho*'
    we will then use these as the key and the value will be the list of nodes that matches this key.
    This will be the adjacency list i.e the edges we will loop through
    This way, the complexity
    We can then use BFS to loop through each node
    We also need a visited state to mark the node as visited
    
    We also need to check if the endword is in the word list. If not, we return 0
    '''
    if endWord not in wordList:
      return 0

    # Build edges
    adjList = defaultdict(list)
    for word in wordList:
      for j in range(len(word)):
        pattern = word[:j] + '*' + word[j+1:]
        adjList[pattern].append(word)
    visited = set([beginWord])
    queue = deque([beginWord])
    res = 1
    while queue:
      for _ in range(len(queue)):
        word = queue.popleft()
        if word == endWord:
          return res
        # get the edges for each pattern of the word and add those edges into the queue
        for j in range(len(word)):
          pattern = word[:j] + '*' + word[j+1:]
          for neighbor in adjList[pattern]:
            if neighbor not in visited:
              queue.append(neighbor)
              visited.add(neighbor)
      res += 1
    return 0
  
sol = Solution()
beginWord = 'hit'
endWord = 'cog'
wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
output = sol.ladderLength(beginWord, endWord, wordList)
print(f'beginWord: {beginWord}\nendWord: {endWord}\nwordList: {wordList}\noutput: {output}')