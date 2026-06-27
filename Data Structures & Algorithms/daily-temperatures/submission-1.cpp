class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size());
        stack<int> temps;
        stack<int> idx;

        temps.push(temperatures[0]);
        idx.push(0);

        for (int i = 1; i < temperatures.size(); ++i){
            while (!temps.empty() && temperatures[i] > temps.top()){
                res[idx.top()] = i - idx.top();
                temps.pop();
                idx.pop();
            }

            temps.push(temperatures[i]);
            idx.push(i);
        }

        return res;
    }
};
