from collections import defaultdict

class TimeMap:

  def __init__(self):
    self.store = defaultdict(list)

  def set(self, key: str, value: str, timestamp: int) -> None:
    self.store[key].append([value, timestamp])
  
  def get(self, key: str, timestamp: int) -> str:
    values = self.store[key]

    l, r = 0, len(values) - 1
    res = ''
    while l <= r:
      m = l + (r - l) // 2
      
      if values[m][1] == timestamp:
        return values[m][0]
      if values[m][1] < timestamp:
        res = values[m][0]
        l = m + 1
      else:
        r = m - 1
        
    return res

timeMap = TimeMap()
timeMap.set('foo', 'bar', 1)
print(timeMap.get('foo', 1))
print(timeMap.get('foo', 3))
timeMap.set('foo', 'bar2', 4)
print(timeMap.get('foo', 4))
print(timeMap.get('foo', 5))

