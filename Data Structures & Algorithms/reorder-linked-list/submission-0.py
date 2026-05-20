# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        temp = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = head
        l2 = slow.next
        slow.next = None

        l2 = self.reverseList(l2)

        res = ListNode()
        current = res

        while l1 or l2:
            if l1:
                current.next = l1
                current = current.next
                l1 = l1.next

            if l2: 
                current.next = l2
                current = current.next
                l2 = l2.next
