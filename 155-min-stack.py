class MinStack:
  stack = None
  def __init__(self):
    self.stack = []

  def push(self, val: int) -> None:
    current_min = val
    if self.stack:
      current_min = min(self.stack[-1][1], current_min)

    self.stack.append([val, current_min])
    
  def pop(self) -> None:
    del self.stack[-1]
    
  def top(self) -> int:
    return self.stack[-1][0]
    
  def getMin(self) -> int:
    return self.stack[-1][1]
  
obj = MinStack()
obj.push(1)
obj.push(3)
obj.push(4)
obj.push(2)
print(f'obj.getMin(): {obj.getMin()}')
obj.pop()
print(f'obj.top(): {obj.top()}')
print(f'obj.getMin(): {obj.getMin()}')
