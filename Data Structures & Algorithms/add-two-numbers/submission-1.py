# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getValue(self, l: ListNode) -> int:
        return l.val if l else 0

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        current = res
        carry = 0
        while l1 or l2:   
            current.next = ListNode(carry)
            current = current.next
            val = self.getValue(l1) + self.getValue(l2)
            if val+carry > 9:
                val -= 10
                carry = 1
            else:
                carry = 0

            current.val += val
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry != 0:
            current.next = ListNode(carry)        

        return res.next