# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        first = head
        second = dummy = ListNode(0, head)

        while True:
            for _ in range(k-1): # find the last node to be reversed
                if not first:
                    return dummy.next
                first = first.next
            if not first:
                return dummy.next    
            temp = first.next # keep the next node under temp
            first.next = None # break the chain
            first = second.next
            # reverse the broken chain
            second.next = self.reverseList(first)
            # re-link the chain and continue to next k-part of chain
            first.next = temp
            second = first
            first = temp
        return dummy.next


