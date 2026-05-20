# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p, q = head, head
        while n > 0:
            q=q.next
            n -= 1
        while q:
            p = p.next
            q = q.next

        res = ListNode()
        current = res

        while head:
            if head == p:
                current.next = p.next
                head = head.next
            else:
                current.next = head
                current = current.next
                head = head.next

        return res.next