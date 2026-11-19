class Solution {
private:
    int dfs(int i, const string& s, vector<int>& cache){
        if (i >= s.length()) return 1;
        if (cache[i] != -1) return cache[i];
        if (s[i] == '0') return 0;

        int groupings = dfs(i+1, s, cache);
        if (i+1 < s.length() && (s[i] == '1' || (s[i] == '2' && s[i+1] <= '6'))){
            groupings += dfs(i+2, s, cache);
        }

        cache[i] = groupings;
        return groupings;
    }
public:
    int numDecodings(string s) {
        vector<int> cache(s.length(), -1);
        return dfs(0, s, cache);
    }
};

