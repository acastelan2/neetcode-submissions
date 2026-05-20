class Node:
    def __init__(self, point: List[int], magnitude: int):
        self.magnitude = magnitude
        self.point = point

    def __lt__(self, other: Node):
        return self.magnitude < other.magnitude

class MinHeap:
    def __init__(self):
        self.heap = [None]

    def push(self, node: Node):
        self.heap.append(node)
        i = len(self.heap)-1
        while i > 1:
            parent = i//2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def pop(self) -> Optional[Node]:
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while True:
            left = i*2
            right = i*2+1
            smallest = i

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
        
        return root

class Solution:
    def __init__(self):
        self.heap = MinHeap()

    def _magnitude(self, point: List[int]) -> int:
        x,y = point
        return x*x + y*y

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            self.heap.push(Node(point, self._magnitude(point)))
        
        for _ in range(k):
            res.append(self.heap.pop().point)
        
        return res