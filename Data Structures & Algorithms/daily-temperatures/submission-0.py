class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_temp = []
        stack_idx = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack_temp and temp > stack_temp[-1]:
                res[stack_idx[-1]] = i - stack_idx[-1]
                stack_idx.pop()
                stack_temp.pop()
                
            stack_temp.append(temp)
            stack_idx.append(i)

        return res