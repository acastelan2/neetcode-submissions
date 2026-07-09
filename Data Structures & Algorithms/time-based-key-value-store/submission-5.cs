public struct TsPair
{
    public string Value { get; }
    public int Timestamp { get; }

    public TsPair(string val, int ts)
    {
        Value = val;
        Timestamp = ts;
    }
}

public class TimeMap {
    private Dictionary<string, List<TsPair>> dict;

    public TimeMap() {
        dict = new Dictionary<string, List<TsPair>>();
    }
    
    public void Set(string key, string value, int timestamp) {
        if (!dict.TryGetValue(key, out var list)){
            list = new List<TsPair>();
            dict[key] = list;
        }
        list.Add(new TsPair(value, timestamp));
    }
    
    public string Get(string key, int timestamp) {
        string res = "";
        if (dict.TryGetValue(key, out var list)){
            int low = 0, high = list.Count-1;
            while (low <= high){
                int mid = low + (high-low) / 2;
                if (list[mid].Timestamp == timestamp){
                    return list[mid].Value;
                } 
                else if (list[mid].Timestamp < timestamp){
                    res = list[mid].Value;
                    low = mid+1;
                }
                else high = mid-1;
            }
        }

        return res;
    }
}


