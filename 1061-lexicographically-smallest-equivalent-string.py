from collections import defaultdict

class Solution:
  def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
    '''
    1. We build a parent map that contains 26 characters being a parent of its own
    2. Next, we go through each character of s1 and s2, and for each iteration, we have 2 operations
      1. find - we get the parent of the characters
      2. union - compare the value of the parents, get the smallest parent, make the smaller parent the parent of the bigger parent, and change the character pointing to the bigger parent to point to the smaller parent instead
    3. we go through each character of the baseStr, and for each iteration, search for the parent of that character. If the character is its own parent, then return that character. Otherwise proceed to get the parent of the parent
    4. append the result for each character and return
    '''

    parents = defaultdict(str)
    result = []
    
    def find(s: str) -> str:
      if not s in parents:
        return s

      if parents[s] == s:
        return s

      return find(parents[s])
    
    def union(c1: str, c2: str):
      p1 = find(c1)
      p2 = find(c2)
      if c1 == c2 or p1 == p2:
        return

      if p1 < p2:
        parents[p2] = p1
        return
      
      parents[p1] = p2
      return
    
    n = len(s1)

    for i in range(n):
      c1 = s1[i]
      c2 = s2[i]
      union(c1, c2)

    for c in baseStr:
      root = find(c)
      result.append(root)
        
    return "".join(result)
  
sol = Solution()
# s1 = 'parker'
# s2 = 'morris'
# baseStr = 'parser'
# s1 = "hello"
# s2 = "world"
# baseStr = "hold"
s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"
print(f'output: {sol.smallestEquivalentString(s1, s2, baseStr)}')
