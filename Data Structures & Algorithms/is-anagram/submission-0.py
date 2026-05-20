class Solution:
    def addToDict(self, hash: dict, input: str):
        for char in input:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1

    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = {},{}
        self.addToDict(dict_s, s)
        self.addToDict(dict_t, t)

        return dict_s == dict_t


        