class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        queries = sorted((q,i) for i,q in enumerate(queries))
        heap = []
        res = [0] * len(queries)
        ptr = 0

        for q,i in queries:
            while ptr < len(intervals) and intervals[ptr][0] <= q:
                heapq.heappush(heap, (intervals[ptr][1]-intervals[ptr][0]+1, intervals[ptr][1]))
                ptr += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
                            
            res[i] = heap[0][0] if heap else -1

        return res