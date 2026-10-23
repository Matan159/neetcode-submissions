# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        temp = head.next
        prev = head
        if count == n:
            return head.next
        for _ in range(count-n-1):
            temp = temp.next
            prev = prev.next
        prev.next =  temp.next
        return head