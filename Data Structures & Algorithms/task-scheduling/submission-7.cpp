class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        array<int, 26> counts{};
        int maxFreq = 0;
        int numMaxFreq = 0;

        for (char task : tasks){
            counts[task - 'A']++;
            maxFreq = max(maxFreq, counts[task - 'A']);
        }

        for (int count : counts){
            if (count == maxFreq){
                numMaxFreq++;
            } 
        }

        size_t res = (maxFreq - 1) * (n+1) + numMaxFreq;
        return max(tasks.size(), res);
    }
};
