class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_dict = {}
        longest_seq = 0

        for num in nums:
            prev_num = num-1
            next_num = num+1
            if num in my_dict:
                continue
            else:
                my_dict[num] = 1
            if prev_num in my_dict:
                my_dict[num] += my_dict[prev_num]
            if next_num in my_dict:
                my_dict[num] += my_dict[next_num]
            while prev_num in my_dict:
                my_dict[prev_num] = my_dict[num]
                prev_num -= 1
            while next_num in my_dict:
                my_dict[next_num] = my_dict[num]
                next_num += 1
            
            if my_dict[num] > longest_seq:
                longest_seq = my_dict[num]

        return longest_seq
        