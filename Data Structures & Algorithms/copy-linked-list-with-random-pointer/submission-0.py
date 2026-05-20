"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}
        current = head

        while current:
            map[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            new_node = map[current]
            new_node.next = map.get(current.next)
            new_node.random = map.get(current.random)
            current = current.next

        return map.get(head)