class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = {}
        l = 0
        max_freq = 0

        for r, c in enumerate(s):
            if c in my_dict:
                my_dict[c] +=1
            else:
                my_dict[c] = 1
            max_freq = max(max_freq, my_dict[c])

            if r-l+1-max_freq > k:
                my_dict[s[l]] -= 1
                l += 1
            
        return len(s)-l