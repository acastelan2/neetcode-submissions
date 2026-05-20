class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        substr = ""
        longest = 0

        for idx, char in enumerate(s):
            if char in my_dict:
                substr = substr[(my_dict[char]+1):] + char
                my_dict = {}
                for i, c in enumerate(substr):
                    my_dict[c] = i
            else:
                my_dict[char] = idx
                substr += char

            longest = max(longest, len(substr))
        return longest