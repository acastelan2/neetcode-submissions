import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-count for _, count in freq.items()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                count = -heapq.heappop(maxHeap)
                count -= 1

                if count > 0:
                    q.append((time+n, count))

            if q and q[0][0] == time:
                task = q.popleft()
                heapq.heappush(maxHeap, -task[1])

        return time
