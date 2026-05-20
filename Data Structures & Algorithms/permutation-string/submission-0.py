class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for c in s1:
            s1_dict[c] = 1 + s1_dict.get(c,0)
        
        l = 0
        s2_dict = {}
        for r in range(len(s2)):
            if s2[l] not in s1_dict:
                l += 1
            if s2[r] in s1_dict:
                s2_dict[s2[r]] = 1 + s2_dict.get(s2[r],0)

            if r-l+1 == len(s1):
                if s1_dict == s2_dict:
                    return True
                else:
                    s2_dict[s2[l]] = s2_dict.get(s2[l],0) - 1
                    l += 1
        return False