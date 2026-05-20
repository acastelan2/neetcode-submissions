class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.popped = []

    def peek(self):
        return self.heap[1]

    def reset(self):
        self.popped = []

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i//2] < self.heap[i]:           
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i//2
    
    def pop(self):        
        self.popped.append(self.peek())
        self.heap[1] = self.heap.pop()

        i = 1
        n = len(self.heap)-1
        while 2*i <= n:
            left = 2*i
            right = 2*i+1
            largest = left
            if right <= n and self.heap[right] > self.heap[left]:
                largest = right
            if self.heap[i] >= self.heap[largest]:
                break
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = MaxHeap()
        self.k = k
        for num in nums:
            self.heap.push(num)

    def add(self, val: int) -> int:
        self.heap.push(val)
        for _ in range(self.k-1):
            self.heap.pop()

        kth = self.heap.peek()
        for p in self.heap.popped:
            self.heap.push(p)

        self.heap.reset()
        return kth
