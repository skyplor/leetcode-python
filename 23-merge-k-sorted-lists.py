from typing import List, Optional
from listnode import ListNode
from listnode_utils import toArray, generateListNodes

class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
      return None

    while len(lists) > 1:
      mergedLists = []
      for i in range(0, len(lists), 2):
        l1 = lists[i]
        l2 = lists[i+1] if (i+1) < len(lists) else None
        mergedLists.append(self.mergeList(l1, l2))
        
      lists = mergedLists
      
    return lists[0]
    
  def mergeList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    while l1 and l2:
      if l1.val < l2.val:
        current.next = l1
        l1 = l1.next
      else:
        current.next = l2
        l2 = l2.next
      current = current.next

    current.next = l1 or l2
    
    return dummy.next

sol = Solution()
list1 = generateListNodes([1,4,5])
list2 = generateListNodes([1,3,4])
list3 = generateListNodes([2,6])
lists = [list1, list2, list3]
output = sol.mergeKLists(lists)
print(f'lists: {lists}\noutput: {toArray(output)}')