public class Solution {
    public int MaxProfit(int[] prices) {
        int res = 0;
        int lowest = prices[0];

        foreach (int price in prices){
            lowest = Math.Min(lowest, price);
            res = Math.Max(res, price-lowest);
        }

        return res;
    }
}
