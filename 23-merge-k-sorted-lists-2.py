from typing import List, Optional
from listnode import ListNode, toArray, generateListNodes
from collections import deque


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        implement mergeTwoLists, each time we pass 2 list to the function. Function returns the merged list
        we have a queue which we traverse, each time we get the next 2 list from the queue and pass into mergeTwoLists. Then we append the result back into the queue
        Once there's less than 2 lists, we return the list in the queue
        Complexity:
          Time: O(N * Log K) - N = number of nodes, K = size of lists
          Space: O(K)
        '''
        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = cur = ListNode()

            while l1 and l2:
                l1_val = l1.val
                l2_val = l2.val
                if l1_val <= l2_val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            elif l2:
                cur.next = l2
            return dummy.next

        queue = deque(l for l in lists)
        while len(queue) > 1:
            l1 = queue.popleft()
            l2 = queue.popleft()
            merged_list = mergeTwoLists(l1, l2)
            queue.append(merged_list)

        if len(queue) > 0:
            return queue.popleft()

        return None


sol = Solution()
list1 = generateListNodes([1, 4, 5])
list2 = generateListNodes([1, 3, 4])
list3 = generateListNodes([2, 6])
lists = [list1, list2, list3]
output = sol.mergeKLists(lists)
print(f'lists: {lists}\noutput: {toArray(output)}')
