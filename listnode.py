from typing import Optional, List

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def toArray(head: Optional['ListNode']) -> Optional['ListNode']:
  res = []
  current = head
  while current:
    res.append(current.val)
    current = current.next
  return res

def generateListNodes(arr: List[int]) -> Optional['ListNode']:
  listNodes = []
  for item in arr:
    listNode = ListNode(item)
    listNodes.append(listNode)

  for i, listNode in enumerate(listNodes):
    if i < len(listNodes) - 1:
      listNode.next = listNodes[i+1]
      
  return listNodes[0]