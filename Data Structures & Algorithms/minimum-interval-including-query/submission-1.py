class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        queries = sorted((q,i) for i,q in enumerate(queries))
        heap = []
        res = [-1] * len(queries)
        ptr = 0

        for q,i in queries:
            while ptr < len(intervals) and intervals[ptr][0] <= q:
                left,right = intervals[ptr]
                heapq.heappush(heap, (right-left+1, right))
                ptr += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                res[i] = heap[0][0]

        return res