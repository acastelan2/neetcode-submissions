struct TsPair {
    string value;
    int timestamp;
};

class TimeMap {
public:
    unordered_map<string, vector<TsPair>> uMap;
    TimeMap(){}
    
    void set(string key, string value, int timestamp) {
        uMap[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        auto it = uMap.find(key);
        if (it != uMap.end()){
            const auto& vec = it->second;

            int low = 0, high = vec.size()-1;
            string res = "";
            while (low <= high){
                int mid = low + (high-low) / 2;
                if (vec[mid].timestamp == timestamp) return vec[mid].value;
                else if (vec[mid].timestamp < timestamp){
                    res = vec[mid].value; 
                    low = mid + 1;   
                }
                else high = mid - 1;
            }

            return res;
        }
        return "";
    }
};
