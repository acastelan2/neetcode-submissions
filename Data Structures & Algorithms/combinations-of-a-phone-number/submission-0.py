import string

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(start, combi):
            if len(combi) == len(digits):
                res.append(combi)
                return
            
            for digit in digits[start:]:
                for j in range(len(mapping[digit])):
                    combi += mapping[digit][j]
                    backtrack(start+1, combi)
                    combi = combi[:-1]
                break

        combi, res = "", []
        if len(digits) > 0:
            letters = string.ascii_lowercase
            mapping = {}
            l = 0
            for digit in range(2, 10):
                i = 3 if digit != 7 and digit != 9 else 4
                mapping[str(digit)] = letters[l:l+i]
                l+=i
            backtrack(0, combi)
        return res