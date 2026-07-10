class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int lowest = prices[0];

        for (int price : prices){
            lowest = min(lowest, price);
            res = max(res, price-lowest);
        }

        return res;
    }
};
