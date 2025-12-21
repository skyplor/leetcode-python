class Solution:
  def robotWithString(self, s: str) -> str:
    '''
    1. create a count of the characters. Since we have only 26 characters, we can have a list of length 26 and value will be the character count
    2. enumerate through each char of s, for each iteration, append c into t and then do Operation 1
    3. Operation 1: peek at the t, is there any other character smaller than t? if no, do Operation 2, otherwise, continue
    4. Operation 2: pop from t and append to p
    '''
    
    characterCount = [0] * 26
    t = []
    p = []
    
    def operationOne(c: str):
      t.append(c)
      characterCount[ord(c) - ord('a')] -= 1
    
    def operationTwo():
      while t:
        robotCharacter = peekRobot()
        maxIdx = ord(robotCharacter) - ord('a')
        for i in range(maxIdx):
          if characterCount[i] > 0:
            return
        c = t.pop()
        p.append(c)
    
    def peekRobot() -> str:
      if len(t) == 0:
        return ''
      return t[-1]
      
    for c in s:
      characterCount[ord(c) - ord('a')] += 1

    for c in s:
      operationOne(c)
      operationTwo()

    n = len(t)
    for _ in range(n):
      operationTwo()
        
    return "".join(p)
  
sol = Solution()
# s = "zza"
# s = "bac"
# s = "bdda"
s = "bydevfziy"
output = sol.robotWithString(s)
print(f"s: {s}, output: {output}")