class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def peek(self):
        return self.heap[1]

    def length(self):
        return len(self.heap)-1

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i//2] < self.heap[i]:           
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i//2
    
    def pop(self):        
        popped = self.peek()
        if self.length() > 1:
            self.heap[1] = self.heap.pop()
        else:
            self.heap.pop()
            
        i = 1
        n = self.length()
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

        return popped

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaxHeap()
        for stone in stones:
            heap.push(stone)
        while heap.length() > 1:
            y = heap.pop()
            x = heap.pop()
            if x < y:
                heap.push(y-x)
        return heap.peek() if heap.length() == 1 else 0

        