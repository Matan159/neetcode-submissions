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
        second = ListNode()
        second.next = head
        first_itteration_flag = True
        while True:
            for _ in range(k-1): # find the last node to be reversed
                if not first or not first.next:
                    return head
                first = first.next
            temp = None if not first else first.next # keep the next node under temp
            first.next = None # break the chain
            first = second.next
            # reverse the broken chain
            second.next = self.reverseList(first)
            if first_itteration_flag: # this will be true only on the first itteration
                head = second.next # this is used to set the head at the right spot after reversing the first k-group
                first_itteration_flag = False
            # re-link the chain and continue to next k-part of chain
            first.next = temp
            second = first
            first = temp
        return head


