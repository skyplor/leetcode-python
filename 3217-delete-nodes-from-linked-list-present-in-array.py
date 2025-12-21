from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        We can convert nums into set and go through head and if a node does not exist in the set, update the prev link to the next link. We will need to keep track of a prev node
        '''
        prev = ListNode(-1, head)
        origin = prev
        cur = head
        remove = set(nums)
        while cur:
            if cur.val in remove:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return origin.next


sol = Solution()
print(
    f'output: {sol.modifiedList([1, 2, 3], ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))}')
print(
    f'output: {sol.modifiedList([1], ListNode(1, ListNode(2, ListNode(1, ListNode(2, ListNode(1, ListNode(2)))))))}')
