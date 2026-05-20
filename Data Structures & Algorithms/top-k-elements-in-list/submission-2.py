class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        buckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            my_dict[num] = 1 + my_dict.get(num,0)
        for num, count in my_dict.items():
            buckets[count].append(num)

        my_list = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                my_list.append(num)
                if len(my_list)  == k:
                    return my_list