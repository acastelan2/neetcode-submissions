class Solution:
    max_len = 3

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            count = len(word)
            encoded += ' ' * (self.max_len - len(str(count))) + str(count) + word
            #subtract from 3 since the length of any word is at most 3 digits (200)
            #result will be either [1, 2 or no whitespace][len of word][word]
        return encoded

    def decode(self, s: str) -> List[str]:        
        decoded = []
        l_Index = 0
        while l_Index < len(s):
            r_Index = l_Index+self.max_len
            len_word = int(s[l_Index:r_Index])
            decoded.append(s[r_Index:r_Index+len_word])
            l_Index += len_word+self.max_len

        return decoded