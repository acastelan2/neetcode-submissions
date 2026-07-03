class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int res = 0;
        int n = heights.size();
        stack<int> stk;

        for (int i = 0; i <= n; ++i){
            while (!stk.empty() && (i == n || heights[i] < heights[stk.top()])){
                int height = heights[stk.top()];
                stk.pop();

                int left = stk.empty() ? -1 : stk.top();
                int width = i - left - 1;

                res = max(res, height*width);
            }

            stk.push(i);
        }

        return res;
    }
};
