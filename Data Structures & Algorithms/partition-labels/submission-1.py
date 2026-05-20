class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indexes = {}
        for i,c in enumerate(s):
            last_indexes[c] = i
        
        res = []
        start = end = 0
        for i,c in enumerate(s):
            end = max(end, last_indexes[c])
            if i == end:
                res.append(end-start+1)
                start = end+1
            
        return res