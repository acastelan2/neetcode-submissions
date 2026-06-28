class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        stack<double> stk;
        vector<pair<int, int>> cars;
        for (int i = 0; i < position.size(); ++i) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.rbegin(), cars.rend());

        double leadingTime;
        for (const auto& [pos,spd] : cars){
            stk.push((double)(target-pos)/spd);
            if (stk.size() > 1 && stk.top() <= leadingTime) stk.pop();
            
            leadingTime = stk.top();
        }

        return stk.size();
    }
};
