class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        self.capacity = capacity
    
    def _insert(self, new_node: ListNode) -> None:
        latest_node = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = latest_node
        latest_node.prev = new_node

    def _remove(self, node: ListNode) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self._insert(node)

        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]


