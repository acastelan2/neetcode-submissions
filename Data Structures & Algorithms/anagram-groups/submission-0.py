class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}

        for word in strs:
            my_list = [0] * 26
            for char in word:
                my_list[ord(char) - ord('a')] += 1
            tup = tuple(my_list)

            if tup in group_dict:
                group_dict[tup].append(word)
            else:
                group_dict[tup] = [word]

        return list(group_dict.values())