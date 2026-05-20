class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(target, start, currCombi, res, lvl):
            if target == 0:
                res.append(currCombi.copy())
                return
            
            lastPopped = 0
            for i in range(start, len(candidates)):
                if candidates[i] == lastPopped or candidates[i] > target:
                    continue
                currCombi.append(candidates[i])
                backtrack(target-candidates[i], i+1, currCombi, res, lvl+1)
                lastPopped = currCombi.pop()

        currCombi, res = [], []
        candidates.sort()
        backtrack(target, 0, currCombi, res,0)
        return res
        