class TimeMap:

    def __init__(self):
        self.my_dict = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.my_dict:
            my_list = self.my_dict[key]
            low = 0
            high = len(my_list)-1
            smallest = ""
            while low <= high:
                mid = low + (high - low) // 2
                if my_list[mid][0] == timestamp:
                    return my_list[mid][1]    
                elif my_list[mid][0] < timestamp:
                    smallest = my_list[mid][1]     
                    low = mid + 1           
                else:
                    high = mid - 1
                    continue
            return smallest
        else:
            return ""
