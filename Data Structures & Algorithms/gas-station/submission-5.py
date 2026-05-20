class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = -1
        tank = 0
        
        for i in range(len(gas)):
            net = gas[i] - cost[i]
            tank += net
            if res == -1 and net >= 0 and tank + 2*net >= 0:
                res = i
            elif res != -1 and tank < 0:
                res = -1            

        return res if tank >= 0 else -1

